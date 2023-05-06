import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from voluntron.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        bio = request.form['bio']
        link = request.form['link']
        db = get_db()
        error = None
        
        if not email:
          error='Email is required'
        elif not password:
           error = 'Password is required'

        if error is None:
          try:
             db.execute(
                "INSERT INTO user (email, password, bio, link) VALUES (?, ?, ?, ?)",
                (email, generate_password_hash(password), bio, link)
             )
             db.commit()
          except db.IntegrityError:
             error = f"An account already exists with the email {email}"
          else:
             return redirect(url_for('auth.login'))
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      db = get_db()
      error = None
      user = db.execute(
         'SELECT * FROM user WHERE email = ?', (email,)
      ).fetchone()

      if user is None:
         error = 'Incorrect email'
      elif not check_password_hash(user['password'], password):
         error = 'Incorrect password.'
      
      if error is None:
         session.clear()
         session['user_id'] = user['id']
         return redirect(url_for('index'))
      flash(error)
   return render_template('auth/login.html')

@bp.before_app_request
def logged_in_user():
   user_id = session.get('user_id')

   if user_id is None:
      g.user = None
   else:
      g.user = get_db().execute(
         'SELECT * FROM user where id = ?', (user_id,)
      ).fetchone()

@bp.route('/logout')
def logout():
   session.clear()
   return redirect(url_for('index'))

def login_required(view):
   @functools.wraps(view)
   def wrapped_view(**kwargs):
      if g.user is None:
        return redirect(url_for('auth.login'))
      return view(**kwargs)
   return wrapped_view