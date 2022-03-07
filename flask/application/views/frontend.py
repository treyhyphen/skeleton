"""Build front end routes."""
from flask import render_template, Blueprint


bp_frontend = Blueprint('frontend', __name__, template_folder='templates')


@bp_frontend.route('/', methods=['GET'])
def index():
    """Index."""
    return render_template('index.html')
