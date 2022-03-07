"""Initialize Flask app.

Returns:
    Flask app.
"""
from flask import Flask, g
from application.views.frontend import bp_frontend
from application.views.api import bp_api
from os import environ, path
from werkzeug.middleware.proxy_fix import ProxyFix
from dotenv import load_dotenv


app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static',
    instance_relative_config=False
)

if path.exists(".env"):
    load_dotenv('.env', verbose=True)
    app.logger.debug("Loaded .env")

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)
app.config.from_object('config.Config')
app.register_blueprint(bp_frontend)
app.register_blueprint(bp_api, url_prefix='/api')


@app.before_request
def app_before_request():
    """Set up g variables that will be useful for all requests."""
    for key in environ.keys():
        if not key.startswith('FLASK_G_'):
            continue
        _key = key.lower().replace('flask_g_', '')
        setattr(g, _key, environ.get(key))
        app.logger.debug(f"Setting g.{_key}={g.get(_key)}")
