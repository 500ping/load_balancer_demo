from flask import Flask
from flask import jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({'ip': request.remote_addr}), 200


if __name__ == '__main__':
    app.run('0.0.0.0')
