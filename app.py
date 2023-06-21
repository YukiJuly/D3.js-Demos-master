import flask
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

# 初始的 pathdata 数据
pathdata = [
    {"path": "AP", "weight": 0.170},
    {"path": "APA", "weight": 0.154},
    {"path": "APC", "weight": 0.144},
    {"path": "APAP", "weight": 0.151},
    {"path": "APCP", "weight": 0.378}
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