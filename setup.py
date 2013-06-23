"""
RMon
-----------

Redis monitor system

Links
`````

* `documentation <http://packages.python.org/Flask-OAuth>`_
* `development version
  <http://github.com/mitsuhiko/flask-oauth/zipball/master#egg=Flask-OAuth-dev>`_
"""
from setuptools import setup


setup(
    name='RMon',
    version='0.1.0',
    url='http://github.com/dgkim84/redis-monitor-temp-repo',
    license='MIT',
    author='',
    author_email='',
    description='Redis monitor system',
    long_description=__doc__,
    py_modules=['RMon'],
    platforms='any',
    install_requires=[
        'Flask==0.9',
        'gevent==0.13.8',
        'gunicorn==0.17.4',
        'Jinja2==2.6',
        'Werkzeug==0.8.3',
        'flask-wtf==0.8.3',
        'redis==2.7.3',
        'flask-assets==0.8',
        'requests==1.2.0'
    ],
    classifiers=[
        'Programming Language :: Python'
    ]
)
