class Configuration:
    def __init__(self):
        self.kv = dict()

    def get(self, key, defaultValue=None):
        return self.kv.get(key, defaultValue)

    def update(self, items):
        self.kv.update(dict(items))
