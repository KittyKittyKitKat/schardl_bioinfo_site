# Copyright (c) 2023 Nyx Harris-Palmer, Tharanie Subramaniam
import csv
import json
from pathlib import Path

from flask import Blueprint, current_app, flash, redirect, render_template, request
from flask_login import login_required, login_user, logout_user

from ..utils.user_model import User, users

routes = Blueprint('routes', __name__)


@routes.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    if email in users and request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        login_user(user)
        flash('Logged in successfully', category='info')
    return redirect(request.referrer)


@routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', category='info')
    return redirect(request.referrer)


@routes.route('/')
@routes.route('/home')
def home():
    images_path = Path(current_app.static_folder) / 'images' / 'slideshow'

    image_names = []
    for image_file in images_path.glob('*'):
        image_names.append(image_file.name)

    return render_template('home.html', title='Home', images=image_names)


@routes.route('/project-details')
def project_details():
    return render_template('project_details.html', title='Project Details')


@routes.route('/biographies')
def biographies():
    with open(Path(current_app.static_folder) / 'biographies.json') as fp:
        bios = json.load(fp)
    return render_template('biographies.html', title='Biographies', bios=bios)


@routes.route('/collection-sites')
def collection_sites():
    view = request.args.get('view')
    view = view if view in ('collection', 'plants') else 'collection'

    if view == 'collection':
        file = 'collection_sites.csv'

    elif view == 'plants':
        file = 'plant_sites.csv'

    with open(
        Path(current_app.static_folder) / file,
        newline='',
    ) as fp:
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
        'collection_sites.html',
        title='Collection Sites',
        markers=markers,
        ecoregions_data=current_app.config['ECOREGIONS_DATA'],
        fieldnames=fieldnames,
        view=view,
    )


@routes.route('/gbrowse')
def gbrowse():
    return render_template('gbrowse.html', title='GBrowse')
