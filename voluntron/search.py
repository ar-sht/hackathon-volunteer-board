from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from thefuzz import process

from voluntron.auth import login_required
from voluntron.db import get_db

bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/', methods=('GET', 'POST'))
def find():
    if request.method == 'POST':
        query = request.form['q']
        db = get_db()
        users = db.execute(
            'SELECT * FROM user'
        ).fetchall()
        bios = [user['bio'] for user in users]
        bio_scores = process.extract(query, bios, limit=100)
        vols = []
        for bio, score in bio_scores:
            if score < 50:
                continue
            pos = [user['bio'] for user in users].index(bio)
            if pos >= 0:
                vols.append(users[pos])
        return render_template('search/index.html', query=query, volunteers=vols)
    return render_template(url_for('index'))
