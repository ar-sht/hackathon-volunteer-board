from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from voluntron.auth import login_required
from voluntron.db import get_db

bp = Blueprint('dashboard', __name__)


@bp.route('/dashboard')
@login_required
def index():
    return render_template("dashboard/index.html")

        
