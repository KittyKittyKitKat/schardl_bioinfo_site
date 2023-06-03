# Copyright (c) 2023 Nyx Harris-Palmer, Tharanie Subramaniam
import csv
import json
from pathlib import Path

from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

STATIC_PATH = Path(__file__).parents[1] / 'static'


@routes.route('/')
@routes.route('/home')
def home():
    with open(STATIC_PATH / 'slideshow_manifest.json') as fp:
        slideshow_images = json.load(fp)
    return render_template('home.html', title='Home', images=slideshow_images)


@routes.route('/project-details')
def project_details():
    return render_template('project_details.html', title='Project Details')


@routes.route('/biographies')
def biographies():
    with open(STATIC_PATH / 'biographies.json') as fp:
        bios = json.load(fp)
    return render_template('biographies.html', title='Biographies', bios=bios)


@routes.route('/collection-sites')
def collection_sites():
    with open(STATIC_PATH / 'collection_sites.csv', newline='') as fp:
        reader = csv.DictReader(fp)
        fieldnames = reader.fieldnames
        markers = []
        for row in reader:
            new_row = {
                key: value if key not in ('Latitude', 'Longitude') else float(value)
                for key, value in row.items()
            }
            markers.append(new_row)
    return render_template(
        'map.html',
        title='Collection Sites',
        markers=markers,
        fieldnames=fieldnames,
    )


@routes.route('/gbrowse')
def gbrowse():
    return render_template('gbrowse.html', title='GBrowse')
