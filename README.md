

## Install

```shell
$ virtualenv env
$ . env/bin/activate
$ python setup install
$ mv config.py.tpl config.py
$ make
$ RMON_SETTINGS=/path/to/config.py gunicorn rmon:app
```
