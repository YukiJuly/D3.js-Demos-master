import flask
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

# 初始的 pathdata 数据
pathdata = [
    {"id": 0, "path": "AP", "weight": 0.170},
    {"id": 1, "path": "APA", "weight": 0.154},
    {"id": 2, "path": "APC", "weight": 0.144},
    {"id": 3, "path": "APAP", "weight": 0.151},
    {"id": 4, "path": "APCP", "weight": 0.378}
];

@app.route('/mypage')
def mypage():
    return flask.send_from_directory('static', 'mypage.html')

# 获取 pathdata 数据的 API 接口
@app.route("/pathdata", methods=["GET"])
def get_pathdata():
    return jsonify(pathdata)

# 保存 pathdata 数据的 API 接口
@app.route("/pathdata", methods=["PUT"])
def put_pathdata():
    global pathdata
    pathdata = request.json
    return jsonify(pathdata)

if __name__ == "__main__":
    app.run(debug=True)