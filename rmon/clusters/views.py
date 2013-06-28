""":mod `rmon.clusters.views` --- rmon clusters views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Blueprint
from flask import request, session, render_template, abort

from rmon.clusters import clusters

mod = Blueprint('cluster', __name__, url_prefix='/v1/clusters')

@mod.route('/')
def index():
    for cluster in clusters.clusters:
        from rmon.processes.redis_process import Redis
        for node in cluster.nodes:
            process = Redis()
            node.info = process.info(node)
    return repr(clusters.clusters)

@mod.route('/<string:id>/nodes', methods=('GET','POST'))
def nodes(id):
    if clusters.get(id) is not None:
        return repr(clusters.get(id))
    abort(404)