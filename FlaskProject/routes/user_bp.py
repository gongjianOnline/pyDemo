from flask import Blueprint, request, jsonify
from decorator.token import token_required

user_bp = Blueprint("user", __name__)
@user_bp.route('/getUserinfo', methods=['GET'])
@token_required
def get_userinfo():
    age = request.args.get('age')
    print("index", age)
    return jsonify({"code": 200, "data": []})