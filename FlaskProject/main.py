from flask import Flask
from routes.user_bp import user_bp
from routes.auth_bp import auth_bp
from routes.admin_bp import admin_bp

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)