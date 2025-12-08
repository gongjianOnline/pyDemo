from flask import Flask, Response, Blueprint
import time

sse_bp = Blueprint("sse", __name__)

@sse_bp.route("/stream")
def stream():
    def event_stream():
        while True:
            # SSE 格式：必须以 "data:" 开头，以两个换行结尾
            yield f"data: 服务器时间 {time.strftime('%H:%M:%S')}\n\n"
            time.sleep(1)  # 每 1 秒推送一次
    return Response(event_stream(), mimetype="text/event-stream")


