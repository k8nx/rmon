""":mod `rmon.commons.views` --- rmon commons views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Blueprint
from flask import request, session, render_template

mod = Blueprint('commons', __name__, url_prefix='')

@mod.route('/')
def index():
    return render_template('index.html')
