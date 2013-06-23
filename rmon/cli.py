""":mod:`rmon.cli` --- rmon CLI scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from rmon import app

__all__ = ('run',)

def run():
    app.run(debug=True, host='0.0.0.0', port=3315)
