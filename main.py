import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "-q"])

from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)

LOGIN = "sofia"

@app.route('/')
def index():
    return Response("Server is running", mimetype='text/plain')

@app.route('/<date_str>')
def date_route(date_str):
    today = datetime.now().strftime('%d%m%y')
    if date_str == today:
        return Response(LOGIN, mimetype='text/plain')
    return Response("Not found", status=404, mimetype='text/plain')

@app.route('/add/<x1>/<x2>')
def add(x1, x2):
    try:
        result = float(x1) + float(x2)
        if result == int(result):
            result = int(result)
        return Response(str(result), mimetype='text/plain')
    except ValueError:
        return Response("Invalid numbers", status=400, mimetype='text/plain')

@app.route('/mpy/<y1>/<y2>')
def mpy(y1, y2):
    try:
        result = float(y1) * float(y2)
        if result == int(result):
            result = int(result)
        return Response(str(result), mimetype='text/plain')
    except ValueError:
        return Response("Invalid numbers", status=400, mimetype='text/plain')

app.run(host='0.0.0.0', port=5000)
