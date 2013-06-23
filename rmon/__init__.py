""":mod:`rmon` --- redis monitor system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Flask

app = Flask(__name__)
app.config.from_envvar('RMON_SETTINGS')

from rmon.commons.views import mod as commonsModule

app.register_blueprint(commonsModule)
