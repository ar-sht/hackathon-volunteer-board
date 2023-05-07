from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from markupsafe import Markup

from voluntron.auth import login_required
from voluntron.db import get_db

bp = Blueprint('dashboard', __name__)


@bp.route('/dashboard')
@login_required
def index():
    print(list(g.user))
    return render_template("dashboard/index.html", bio=Markup(g.user['bio']))

        
