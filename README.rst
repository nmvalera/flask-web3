.. image:: https://travis-ci.org/nmvalera/flask-web3.svg?branch=master
    :target: https://travis-ci.org/nmvalera/flask-web3
    :alt: Build Status

.. image:: https://codecov.io/gh/nmvalera/flask-web3/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/nmvalera/flask-web3
    :alt: Coverage

.. image:: https://readthedocs.org/projects/flask-web3/badge/?version=stable
    :target: https://flask-web3.readthedocs.io/en/stable/?badge=stable
    :alt: Documentation Status

Flask-Web3
==========

Flask-Web3 is a flask extension allowing to smoothly integrate a flask application with `web3.py`_.
This package is intended for developers will to build a Flask application that interacts with an Ethereum client.

.. _`web3.py`: https://github.com/ethereum/web3.py

Requirements
~~~~~~~~~~~~

- Python>=3.5

A simple example
~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> from flask import Flask, jsonify
    >>> from flask_web3 import current_web3, FlaskWeb3

    # Declare Flask application
    >>> app = Flask(__name__)

    # Set Flask-Web3 configuration
    >>> app.config.update({'ETHEREUM_PROVIDER': 'http', 'ETHEREUM_ENDPOINT_URI': 'http://localhost:8545'})

    # Declare Flask-Web3 extension
    >>> web3 = FlaskWeb3(app=app)

    # Declare route
    >>> @app.route('/blockNumber')
    ... def block_number():
    ...     return jsonify({'data': current_web3.eth.blockNumber})

You can notice that Flask-Web3 gives you an application context bound variable ``current_web3`` that is accessible
from any active flask application context.

An advanced example
~~~~~~~~~~~~~~~~~~~

You may like to declare your Flask-Web3 extension from a customize Web3 class with enhanced logic.

.. code-block:: python

    >>> from flask import Flask, jsonify
    >>> from flask_web3 import current_web3, FlaskWeb3
    >>> from web3 import Web3

    # Declare Flask application
    >>> app = Flask(__name__)
    >>> app.config.update({'ETHEREUM_PROVIDER': 'http', 'ETHEREUM_ENDPOINT_URI': 'http://localhost:8545'})

    # Declare a custom Web3 class
    >>> class CustomWeb3(Web3):
    ...     def customBlockNumber():
    ...         return self.eth.blockNumber

    # Associate a custom FlaskWeb3 extension
    >>> class CustomFlaskWeb3(FlaskWeb3):
    ...     web3_class = CustomWeb3

    # Declare customized web3 extension
    >>> web3 = CustomFlaskWeb3(app=app)
    >>> isinstance(web3, CustomWeb3)
    True

    # Declare route
    >>> @app.route('/customBlockNumber')
    ... def last_odd_block_number():
    ...     return jsonify({'data': current_web3.customBlockNumber()})

Documentation
~~~~~~~~~~~~~

Full documentation is available at https://flask-web3.readthedocs.io/en/stable/.