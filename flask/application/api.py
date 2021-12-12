"""Build API routes."""
from flask import jsonify, Blueprint, request, url_for

bp_api = Blueprint('api', __name__)


@bp_api.route('/sup_world', methods=['GET'])
def sup_world():
    """Return JSON from a database."""
    from application.db import DB
    db = DB()
    result = db.select_one("select * from skeleton")
    return jsonify(result)


@bp_api.route('/url_test', methods=['GET'])
def url_test():
    """Test URLs returned by Flask.

    Returns:
        string: JSON document of different URLs and paths
    """
    return jsonify({
        'base_url': request.base_url,
        'url_rule': str(request.url_rule),
        'request_path': request.path,
        'request_url': request.url,
        'request_host': request.host,
        'request_host_url': request.host_url,
        'host_header': request.headers.get('X-Forwarded-Host'),
        'url_for': url_for('api.url_test')
    })
