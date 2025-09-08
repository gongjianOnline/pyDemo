import os
from flask import Flask,send_from_directory
from routes.user_bp import user_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASEDIR = os.path.dirname(os.path.abspath(__file__))
FE_DIR = os.path.join(BASEDIR, "frontend", "dist")
# 静态资源
@app.route('/<path:filepath>')
def fe_assets(filepath):
    return send_from_directory(FE_DIR, filepath)
# 入口页
@app.route('/')
def fe_index():
    return send_from_directory(FE_DIR, 'index.html')


# 注册蓝图
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)