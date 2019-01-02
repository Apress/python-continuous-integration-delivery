#!/usr/bin/python3

from flask import Flask, request

from matheval.evaluator import math_eval

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tree = request.get_json(force=True)
    result = math_eval(tree);
    return str(result) + "\n"

if __name__ == '__main__':
    app.run(debug=True)
