# rmon

## Install

```shell
$ virtualenv env
$ . env/bin/activate
$ python setup install
$ mv config.py.tpl config.py
$ make
$ RMON_SETTINGS=/path/to/config.py gunicorn rmon:app
```

## Screenshots

차트가 빠진 형태. 프로토타이핑 (2013.06.28)

![RMon-M1](https://github.com/dgkim84/rmon/blob/master/docs/images/m1.png?raw=true "rmon-m1")
