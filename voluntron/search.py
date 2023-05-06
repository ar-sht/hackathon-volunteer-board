from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from voluntron.auth import login_required
from voluntron.db import get_db

bp = Blueprint('search', __name__, url_prefix='/search')
