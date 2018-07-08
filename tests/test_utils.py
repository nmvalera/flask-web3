"""
    tests.test_utils
    ~~~~~~~~~~~~~~~~

    Test utilities

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see LICENSE for more details.
"""

import pytest
from web3 import EthereumTesterProvider, HTTPProvider, WebsocketProvider, IPCProvider

from flask_web3.utils import create_provider


def test_create_provider():
    test_provider = create_provider({'ETHEREUM_PROVIDER': 'test'})
    assert isinstance(test_provider, EthereumTesterProvider)

    http_provider = create_provider({'ETHEREUM_PROVIDER': 'http', 'ETHEREUM_ENDPOINT_URI': 'http:localhost:8545'})
    assert isinstance(http_provider, HTTPProvider)

    ws_provider = create_provider({'ETHEREUM_PROVIDER': 'ws', 'ETHEREUM_ENDPOINT_URI': 'ws:localhost:8545'})
    assert isinstance(ws_provider, WebsocketProvider)

    ipc_provider = create_provider({'ETHEREUM_PROVIDER': 'ipc', 'ETHEREUM_IPC_PATH': '/path/to/ipc'})
    assert isinstance(ipc_provider, IPCProvider)

    with pytest.raises(Exception):
        create_provider({'ETHEREUM_PROVIDER': 'unknown'})
