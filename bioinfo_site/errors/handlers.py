# Copyright (c) 2023 Nyx Harris-Palmer, Tharanie Subramaniam
from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(401)
def error_401(error):
    return render_template('errors/401.html'), 401


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(405)
def error_405(error):
    return render_template('errors/405.html'), 405
