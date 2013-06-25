"""
rmon
----

redis monitor system
"""
from setuptools import setup, find_packages

setup(
    name='rmon',
    version='0.1.0',
    url='http://github.com/dgkim84/redis-monitor-temp-repo',
    license='MIT',
    packages=find_packages(),
    author='',
    author_email='',
    description='redis monitor system',
    long_description=__doc__,
    py_modules=['rmon'],
    platforms='any',
    entry_points={
        'console_scripts': [
        ]
    },
    install_requires=[
        'Flask==0.9',
        'gevent==0.13.8',
        'gunicorn==0.17.4',
        'Jinja2==2.6',
        'Werkzeug==0.8.3',
        'flask-wtf==0.8.3',
        'flask-assets==0.8',
        'requests==1.2.0',
        'redis==2.7.6',
        'pubsub==0.1.1'
    ],
    classifiers=[
        'Programming Language :: Python'
    ]
)
