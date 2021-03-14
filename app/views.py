from flask import Blueprint

blueprint = Blueprint('views', __name__)


@blueprint.route('/')
def home():
    return {'status': True}
