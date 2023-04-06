from flask import render_template, Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/home')
def home():
    return render_template('home.html', title='Home')


@routes.route('/project-details')
def project_details():
    return render_template('project_details.html', title='Project Details')


@routes.route('/biographies')
def biographies():
    return render_template('biographies.html', title='Biographies')


@routes.route('/map')
def map():
    return render_template('map.html', title='Map')