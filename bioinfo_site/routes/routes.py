from pathlib import Path
from flask import render_template, Blueprint, url_for

routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/home')
def home():
    slideshow_images = []
    slideshow_images_path = Path(__name__.split('.')[0]) / 'static' / 'images' / 'slideshow'
    for image_file in slideshow_images_path.glob('*'):
        static_filename = str(Path(*image_file.parts[1:]))
        aspect_ratio = 'is-4by3' if image_file.stem.endswith('_l') else 'is-3by4'
        slideshow_images.append((static_filename, aspect_ratio))
    return render_template('home.html', title='Home', images=slideshow_images)


@routes.route('/project-details')
def project_details():
    return render_template('project_details.html', title='Project Details')


@routes.route('/biographies')
def biographies():
    return render_template('biographies.html', title='Biographies')


@routes.route('/map')
def map():
    return render_template('map.html', title='Map')


@routes.route('/gbrowse')
def gbrowse():
    return render_template('gbrowse.html', title='GBrowse')