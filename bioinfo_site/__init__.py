# Copyright (c) 2023 Nyx Harris-Palmer, Tharanie Subramaniam
import json
from pathlib import Path

from flask import Flask


def create_app():
    app = Flask(__name__)
    from bioinfo_site.errors.handlers import errors
    from bioinfo_site.routes.routes import routes

    with open(Path(app.static_folder) / 'Ky_Level_IV_Ecoregions.geojson', 'r') as fp:
        app.config['ECOREGIONS_DATA'] = json.load(fp)

    app.register_blueprint(routes)
    app.register_blueprint(errors)
    return app
