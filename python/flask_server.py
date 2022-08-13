from flask import Flask, jsonify, request, abort
import bitcoin_output
from os import environ

app = Flask(__name__)

password = environ['MY_PASS']

@app.route("/", methods=["GET"])
def summary():
    headers = request.headers
    auth = headers.get("x-Api-Key")
    if auth == password:
        return jsonify(bitcoin_output.showJson())
    else:
        abort(401)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
