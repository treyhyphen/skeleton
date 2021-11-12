"""Initialize Flask app.

Returns:
    Flask app.
"""
from flask import Flask, g
from os import environ
from .frontend import bp_frontend
from .api import bp_api
from .db import DB

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static',
    instance_relative_config=False
)
app.config.from_object('config.Config')


def create_app():
    """Construct the core application."""
    app.register_blueprint(bp_frontend)
    app.register_blueprint(bp_api, url_prefix='/api')

    return app
