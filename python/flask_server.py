from flask import Flask, jsonify
import bitcoin_output

app = Flask(__name__)

@app.route("/")
def summary():
    return jsonify(bitcoin_output.showJson())

if __name__ == "__main__":
    app.run(host='0.0.0.0')

