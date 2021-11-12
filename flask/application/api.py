"""Build API routes."""
from flask import jsonify, Blueprint

bp_api = Blueprint('api', __name__)


@bp_api.route('/sup_world', methods=['GET'])
def sup_world():
    """Return JSON from a database."""
    from application.db import DB
    db = DB()
    result = db.select_one("select * from skeleton")
    return jsonify(result)
