from flask import Blueprint, request, jsonify

from database.db2 import get_by_id

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/userList", methods=['POST'])
def user_list():
    # data = request.json
    # print(data)
    # print(data['user'])
    row = get_by_id("tb_subject", "name", "python真傻逼")
    return jsonify({"code":200,"data":row,"message":"success"})
