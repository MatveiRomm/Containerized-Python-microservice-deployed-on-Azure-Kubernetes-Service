from flask import Flask, jsonify, request
import bitcoin_output

jsnData = bitcoin_output.data

app = Flask(__name__)

@app.route("/")
def summary():
    return jsonify(jsnData)
