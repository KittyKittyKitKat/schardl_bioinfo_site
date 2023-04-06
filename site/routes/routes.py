from flask import render_template, Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/home')
def home():
    return render_template('home.html', title='Home')

@routes.route('/page2')
def page2():
    return render_template('page2.html', title='Page 2')
