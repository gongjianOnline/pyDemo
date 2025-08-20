from flask import Blueprint, request, jsonify
# from database.db import fetch_one
from decorator.token import token_required

user_bp = Blueprint("user", __name__)
@user_bp.route('/getUserinfo', methods=['GET'])
@token_required
def get_userinfo():
    # result = fetch_one("select * from tb_subject")
    age = request.args.get('age')
    print("index", age)
    # return jsonify({"code": 200, "data": result})
    return jsonify({"code": 200, "data": []})