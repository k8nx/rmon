from . import Process

import redis

class Redis(Process):
    def info(self, node):
        r = redis.StrictRedis(host=node.hostname, port=node.port, db=0)
        try:
            return r.info()
        except:
            pass
        return {}