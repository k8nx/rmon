""":mod `rmon.clusters.views` --- rmon clusters views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Blueprint
from flask import request, session, render_template

from rmon.clusters import clusters

import json

mod = Blueprint('cluster', __name__, url_prefix='/v1/clusters')

@mod.route('/')
def index():
    return json.dumps(clusters.ids)

@mod.route('/<string:id>/nodes', methods=('GET','POST'))
def nodes():
    if clusters.get(id) is not None:
        return json.dumps(clusters.get(id).nodes)