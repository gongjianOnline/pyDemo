from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    print('user', user)
    return jsonify({"code": 200, "message": "请求成功"})