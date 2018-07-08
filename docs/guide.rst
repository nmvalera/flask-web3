About Flask-Web3
================

Flask-Web3 is a flask extension allowing to smoothly integrate a flask application with `web3.py`_.
This package is intended for developers will to build a Flask application that interacts with an Ethereum client.

This page gives a good introduction to Flask-Web3. If not yet install please refer to the Installation section.

It is recommended that you have some light knowledge of `web3.py`_ before you try
working with Flask-Web3.

.. _`web3.py`: https://github.com/ethereum/web3.py

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

Flask-Web3 configuration
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :widths: 30 50 20
    :header-rows: 1

    * - Key
      - Comment
      - Default

    * - ``ETHEREUM_PROVIDER``
      - Type of Ethereum provider to use can be one of ``http``, ``ipc``, ``ws`` or ``test``
      - ``http``

    * - ``ETHEREUM_ENDPOINT_URI``
      - Endpoint URI of Ethereum client (only useful when provider is ``http`` or ``ws``)
      - ``http``

    * - ``ETHEREUM_IPC_PATH``
      - IPC path of Ethereum client (only useful when provider is ``ipc``)
      - None

    * - ``ETHEREUM_OPTS``
      - A dictionary containing extra options fed to the provider when declaring it
      - ``{}``