"""Initialize Flask app.

Returns:
    Flask app.
"""
from flask import Flask, g
from .frontend import bp_frontend
from .api import bp_api
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static',
    instance_relative_config=False
)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)
app.config.from_object('config.Config')
app.register_blueprint(bp_frontend)
app.register_blueprint(bp_api, url_prefix='/api')
