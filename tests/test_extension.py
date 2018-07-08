"""
    tests.test_extension
    ~~~~~~~~~~~~~~~~~~~~

    Test Flask-Web3 extension

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see LICENSE for more details.
"""

import json

import pytest
from web3 import Web3

from flask_web3 import FlaskWeb3, current_web3


def test_extension_meta_class():
    assert issubclass(FlaskWeb3, Web3)

    web3_extension = FlaskWeb3()

    assert isinstance(web3_extension, Web3)
    assert isinstance(web3_extension, FlaskWeb3)


def test_extension_meta_class_with_inheritance():
    class Web3Test(Web3):
        """Class used for test"""

    class FlaskWeb3Test(FlaskWeb3):
        web3_class = Web3Test

    assert issubclass(FlaskWeb3Test, Web3)

    web3_extension = FlaskWeb3Test()

    assert isinstance(web3_extension, Web3Test)
    assert isinstance(web3_extension, FlaskWeb3)

    class FlaskWeb3Test(FlaskWeb3):
        """Class used for test"""

    assert issubclass(FlaskWeb3Test, Web3)


def test_extension_meta_class_with_invalid_inheritance():
    class InvalidWeb3Test:
        """Class used for test"""

    with pytest.raises(AssertionError):
        class TestFlaskWeb3(FlaskWeb3):
            web3_class = InvalidWeb3Test


def test_extension_with_app(app):
    class Web3Test(Web3):
        """Class used for test"""

    class FlaskWeb3Test(FlaskWeb3):
        web3_class = Web3Test

    web3_extension = FlaskWeb3(app=app)

    assert hasattr(app, 'web3')
    assert app.web3 == web3_extension


def test_extension(web3_app):
    with pytest.raises(RuntimeError):
        print(current_web3.eth.blockNumber)

    with web3_app.test_client() as c:
        response = c.get('/blockNumber')
    assert response.status_code == 200
    assert json.loads(response.data.decode()) == {'data': 0}

    with web3_app.test_client() as c:
        response = c.get('/sendTransaction')
    assert response.status_code == 200
    assert json.loads(response.data.decode()) == {
        'data': '0xa65bd0af37e8be53432cf263cf7fe28275c2182df84e0bacfc4eafcf438159bc',
    }

    with web3_app.test_client() as c:
        response = c.get('/blockNumber')
    assert response.status_code == 200
    assert json.loads(response.data.decode()) == {'data': 1}


def test_invalid_extension(invalid_web3_app):
    with invalid_web3_app.test_client() as c:
        response = c.get('/blockNumber')

    assert response.status_code == 500
