import json

class Cluster:
    def __init__(self, id, type, nodes):
        self.id = id
        self.type = type
        self.nodes = nodes

    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Node:
    def __init__(self, name, hostname, port):
        self.name = name
        self.hostname = hostname
        self.port = port
        self.info = None

    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)