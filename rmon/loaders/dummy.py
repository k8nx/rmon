from rmon.loaders import Loader
from rmon.commons.models import Cluster, Node

class DummyLoader(Loader):
    def load(self):
        cluster = Cluster(id, [
            Node('redis-1', 'localhost', 6379)
        ])
        return [cluster]