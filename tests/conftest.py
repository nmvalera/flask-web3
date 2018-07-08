"""
    tests.conftest
    ~~~~~~~~~~~~~~

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see LICENSE for more details.
"""

import os

import pytest
from flask import Flask, jsonify

from flask_web3 import FlaskWeb3, current_web3

TEST_DIR = os.path.dirname(__file__)


@pytest.fixture(scope='function')
def app():
    _app = Flask('test-app')

    yield _app


@pytest.fixture(scope='function')
def web3_app(app):
    app.config['ETHEREUM_PROVIDER'] = 'test'

    FlaskWeb3(app=app)

    @app.route('/blockNumber')
    def block_number():
        return jsonify({'data': current_web3.eth.blockNumber})

    @app.route('/sendTransaction')
    def send_transaction():
        tx = {
            'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
            'from': current_web3.eth.accounts[0],
            'value': 12345
        }

        tx_hash = current_web3.eth.sendTransaction(tx)

        return jsonify({'data': tx_hash.hex()})

    yield app


@pytest.fixture(scope='function')
def invalid_web3_app(app):
    # We do to init FlaskWeb3 extension
    app.config['ETHEREUM_PROVIDER'] = 'test'

    @app.route('/blockNumber')
    def block_number():
        return jsonify({'data': current_web3.eth.blockNumber})

    yield app
