# Copyright (c) 2023 Nyx Harris-Palmer, Tharanie Subramaniam
from flask import Flask


def create_app():
    app = Flask(__name__)
    from bioinfo_site.routes.routes import routes
    from bioinfo_site.errors.handlers import errors

    app.register_blueprint(routes)
    app.register_blueprint(errors)
    return app
