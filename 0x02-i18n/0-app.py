#!/usr/bin/env python3

""" 0-app.py. Create a single / route and an index.html"""

from flask import Flask, render_template

app = Flask(__name__)

app.route('/', strict_slashes=False)
def index() -> str:
    """ renders html page"""
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port: '5000', debug=True)
