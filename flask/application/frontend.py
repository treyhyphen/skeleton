"""Build front end routes."""
from flask import render_template, request, g, Blueprint
from flask import current_app
from os import environ


bp_frontend = Blueprint('frontend', __name__, template_folder='templates')


@bp_frontend.before_request
def before_request_func():
    """Handle reverse proxy requests and set up Flask 'g' from ENV."""
    base_url = request.base_url
    if 'X-Forwarded-Host' in request.headers:
        base_url = f"https://{request.headers.get('X-Forwarded-Host')}"

    base_url_parts = base_url.split('/')
    if len(base_url_parts) > 3:
        base_url = '/'.join(base_url_parts[:3])

    g.base_url = base_url

    for key in environ.keys():
        if not key.startswith('FLASK_G_'):
            continue
        _key = key.lower().replace('flask_g_', '')
        setattr(g, _key, environ.get(key))
        current_app.logger.debug(f"{_key}={g.get(_key)}")

    current_app.logger.debug(f"Headers:\n{request.headers}")


@bp_frontend.route('/', methods=['GET'])
def index():
    """Index."""
    return render_template('index.html')
