"""
    flask_web3
    ~~~~~~~~~~

    A flask extensions allowing to smoothly integrate with web3.py Ethereum interface
    (c.f. https://github.com/ethereum/web3.py)

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see :ref:`license` for more details.
"""

from .extension import FlaskWeb3
from .locals import current_web3

__version__ = '0.1.1'

__all__ = [
    'FlaskWeb3',
    'current_web3',
]
