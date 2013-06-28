""":mod `rmon.clusters.views` --- rmon clusters views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Blueprint
from flask import request, session, render_template, abort

from rmon.clusters import clusters

mod = Blueprint('cluster', __name__, url_prefix='/v1/clusters')

@mod.route('/')
def index():
    return repr(clusters.clusters)

@mod.route('/<string:id>/nodes', methods=('GET','POST'))
def nodes(id):
    if clusters.get(id) is not None:
        return repr(clusters.get(id))
    abort(404)