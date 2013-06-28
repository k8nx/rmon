from rmon.core import Configuration
from rmon.loaders import Loader

class Clusters:
    def __init__(self):
        self.loader = None
        self.config = Configuration()
        self.clusters = self.load()
        self.ids = map(lambda c: c.id, self.clusters)

    def update(self, kv):
        self.config.update(kv)

    def get(self, id):
        for cluster in self.clusters:
            if cluster.id == id:
                return cluster
        return None

    def load(self):
        if self.loader is None:
            fullname = self.config.get('NODE_LOADER', 'rmon.loaders.dummy')
            if '.' in fullname:
                package, name = fullname.rsplit('.', 1)
            else:
                package = 'rmon.loaders'
                name = fullname

            try:
                self.module = __import__('%s.%s'%(package, name)).loaders
            except ImportError as e:
                # TODO:
                raise e
            if hasattr(self.module, name):
                self.loader = getattr(self.module, name)
                return self.loader.load()
            else:
                return None

