""":mod:`rmon` --- redis monitor system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Flask

app = Flask(__name__, static_folder='assets', static_url_path='/assets')
app.config.from_envvar('RMON_SETTINGS')

from rmon.commons.views import mod as commonsModule

app.register_blueprint(commonsModule)
