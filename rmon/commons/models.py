
class Cluster:
    def __init__(self, id, nodes):
        self.id = id
        self.nodes = nodes

class Node:
    def __init__(self, name, hostname, port):
        self.name = name
        self.hostname = hostname
        self.port = port