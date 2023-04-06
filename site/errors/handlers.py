from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error: HTTPException):
    return render_template('errors/404.html'), 404
