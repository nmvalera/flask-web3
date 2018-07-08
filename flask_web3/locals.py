"""
    flask_web3.locals
    ~~~~~~~~~~~~~~~~~

    Implement Flask context bounded object to access web3 instances

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see :ref:`license` for more details.
"""

from flask import _app_ctx_stack, current_app
from werkzeug.local import LocalProxy


def _get_web3():
    if _app_ctx_stack.top is None:
        raise RuntimeError(
            "Cannot access current_web3 when outside of an application "
            "context.")
    app = current_app._get_current_object()
    if not hasattr(app, "web3"):
        raise AttributeError(
            "{0} has no 'web3' attribute. You need to initialize it "
            "with a FlaskWeb3 extensions.".format(app))
    return app.web3


current_web3 = LocalProxy(_get_web3)
