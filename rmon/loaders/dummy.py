from rmon.loaders import Loader
from rmon.commons.models import Cluster, Node

class DummyLoader(Loader):
    def load(self):
        cluster1 = Cluster('redis-cluster-1', 'redis', [
            Node('redis-1:1', 'localhost', 6379),
            Node('redis-1:2', 'localhost', 6380),
            Node('redis-1:3', 'localhost', 6381)
        ])
        cluster2 = Cluster('redis-cluster-2', 'redis', [
            Node('redis-2:1', 'localhost', 7379),
            Node('redis-2:2', 'localhost', 7380),
            Node('redis-2:3', 'localhost', 7381)
        ])
        return [cluster1, cluster2]