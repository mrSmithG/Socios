from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
#from .forms import NameForm
from flask_login import login_required, current_user
from .. import db
from ..models import User



@main.route('/')
def sign_in_or_sign_up():
    return render_template('first_page.html')

@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', user=user)

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

