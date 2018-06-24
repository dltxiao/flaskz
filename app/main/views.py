from datetime import datetime
from flask import render_template, session, redirect, url_for
from flask_login import login_required

from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    return render_template('index.html', form=form, current_time=datetime.utcnow())

@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated user are allowed!'
