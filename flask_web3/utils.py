from web3 import HTTPProvider, WebsocketProvider, EthereumTesterProvider, IPCProvider

from .config import ETHEREUM_PROVIDER, ETHEREUM_OPTS, ETHEREUM_ENDPOINT_URI, ETHEREUM_IPC_PATH


def create_provider(config):
    """Create a web3.py provider

    :param config: Provider configuration
    :type config: dict
    """
    provider, opts = config.get('ETHEREUM_PROVIDER', ETHEREUM_PROVIDER), config.get('ETHEREUM_OPTS', ETHEREUM_OPTS)

    if provider == 'http':
        return HTTPProvider(endpoint_uri=config.get('ETHEREUM_ENDPOINT_URI', ETHEREUM_ENDPOINT_URI), **opts)

    elif provider == 'ipc':
        return IPCProvider(ipc_path=config.get('ETHEREUM_IPC_PATH', ETHEREUM_IPC_PATH), **opts)

    elif provider == 'ws':
        return WebsocketProvider(endpoint_uri=config.get('ETHEREUM_ENDPOINT_URI', ETHEREUM_ENDPOINT_URI), **opts)

    elif provider == 'test':
        return EthereumTesterProvider()

    else:
        raise Exception("'ETHEREUM_PROVIDER' configuration must be one of 'http', 'ipc', 'ws', 'test'")
