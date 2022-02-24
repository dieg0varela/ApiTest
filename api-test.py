from crypt import methods
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello():
    return jsonify({'data': 'Hello World from Flask'})

if __name__ == '__main__':
    app.run(debug = True)