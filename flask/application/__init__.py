"""Initialize Flask app.

Returns:
    Flask app.
"""
from flask import Flask, g
from .frontend import bp_frontend
from .api import bp_api

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static',
    instance_relative_config=False
)
app.config.from_object('config.Config')
app.register_blueprint(bp_frontend)
app.register_blueprint(bp_api, url_prefix='/api')
