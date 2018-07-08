"""
    flask_web3.extension
    ~~~~~~~~~~~~~~~~~~~~

    Flask-Web3 extension

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see :ref:`license` for more details.
"""

from collections import OrderedDict

from web3 import Web3

from .utils import create_provider as _create_provider


class FlaskWeb3Meta(type):
    """Meta class for Flask-Web3 extension"""

    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()

    def __new__(mcs, name, bases, ns):
        web3_class = ns.pop('web3_class', None)
        if web3_class is not None:
            assert issubclass(web3_class, Web3), "web3_class must be a subclass of `web3.Web3` class " \
                                                 "but you provided {}".format(web3_class)
            bases = bases + (web3_class,)

        return super().__new__(mcs, name, bases, dict(ns))


class FlaskWeb3(metaclass=FlaskWeb3Meta):
    """Main class for declaring a flask extension

    :param app: Flask application or blueprint object to extend
    :type app: flask.Flask
    :param create_provider: Function used to create a Web3 provider
    :type create_provider: A function taking a :class:flask.Flask application configuration as parameter
    """

    # Web3 class to use for
    web3_class = Web3

    def __init__(self, *args, app=None, create_provider=_create_provider, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_provider = create_provider
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Initialize application

        :param app: Flask application or blueprint object to extend
        :type app: flask.Flask
        """

        # Create a provider
        self.providers = self.create_provider(app.config)

        # Attached the extension to the app
        app.web3 = self
