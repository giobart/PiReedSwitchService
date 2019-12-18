from flask import Blueprint, jsonify
from flask_jwt_extended import (jwt_required, get_jwt_identity)

service = Blueprint('service', __name__)


@service.route('/api/service', methods=['GET'])
@jwt_required
def my_service():
    # check user identity from the access token
    identity = get_jwt_identity()

    if identity:
        resp = jsonify({
            'message': 'Hello World',
        })

        return resp, 200
    else:
        return 405


@service.route('/api/test', methods=['GET'])
def my_test():
    resp = jsonify({
        'message': 'Hello World',
    })

    return resp, 200
