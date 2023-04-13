# Copyright (c) 2023 Nyx Harris-Palmer, Tharanie Subramaniam
import json
from pathlib import Path

from flask import Blueprint, render_template, url_for

routes = Blueprint('routes', __name__)


@routes.route('/')
@routes.route('/home')
def home():
    slideshow_images = []
    slideshow_images_path = (
        Path(__name__.split('.')[0]) / 'static' / 'images' / 'slideshow'
    )
    for image_file in slideshow_images_path.glob('*'):
        slideshow_images.append(str(Path(*image_file.parts[1:])))
    return render_template('home.html', title='Home', images=slideshow_images)


@routes.route('/project-details')
def project_details():
    return render_template('project_details.html', title='Project Details')


@routes.route('/biographies')
def biographies():
    with open(Path(__name__.split('.')[0]) / 'static' / 'biographies.json') as fp:
        bios = json.load(fp)
    return render_template('biographies.html', title='Biographies', bios=bios)


@routes.route('/map')
def map():
    return render_template('map.html', title='Map')


@routes.route('/gbrowse')
def gbrowse():
    return render_template('gbrowse.html', title='GBrowse')
