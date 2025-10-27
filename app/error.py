from flask import Blueprint, render_template
from app import db

bp_error = Blueprint('errors', __name__)

@bp_error.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@bp_error.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

