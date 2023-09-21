# Copyright (c) 2023 Nyx Harris-Palmer, Tharanie Subramaniam
import json
from pathlib import Path

import flask_login
from dotenv import dotenv_values
from flask import Flask

login_manager = flask_login.LoginManager()


def create_app():
    app = Flask(__name__)
    app.secret_key = dotenv_values()['SECRET_KEY']
    login_manager.init_app(app)
    from bioinfo_site.errors.handlers import errors
    from bioinfo_site.routes.routes import routes

    with open(Path(app.static_folder) / 'Ky_Level_IV_Ecoregions.geojson', 'r') as fp:
        app.config['ECOREGIONS_DATA'] = json.load(fp)

    app.register_blueprint(routes)
    app.register_blueprint(errors)
    return app
