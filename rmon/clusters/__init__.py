from .base import Clusters

import imp
import os

settings = os.environ.get('RMON_SETTINGS')
config = imp.new_module('config')
config.__file__ = settings
try:
    with open(settings) as config_file:
        exec(compile(config_file.read(), settings, 'exec'), config.__dict__)
except IOError as e:
    e.strerror = 'Unable to load configuration. - %s'%(e.strerror,)
    raise e

clusters = Clusters()
clusters.update(config.__dict__)