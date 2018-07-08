"""
    flask_web3.config
    ~~~~~~~~~~~~~~~~~

    Default Flask-Web3 configuration

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see :ref:`license` for more details.
"""

#: Indicate the type of provider you would like to use, can be either 'http', 'ipc', 'ws' or 'tester'
ETHEREUM_PROVIDER = 'http'

#: URI of the Ethereum client to connect to
ETHEREUM_ENDPOINT_URI = 'http://localhost:8545'

#: IPC path of the Ethereum client to connect to
ETHEREUM_IPC_PATH = None

#: Extra options for provider declaration
ETHEREUM_OPTS = {}
