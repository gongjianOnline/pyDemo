from flask import Blueprint, request

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/userList", methods=['POST'])
def user_list():
    data = request.json
    print(data)
    print(data['user'])
    return "json"
