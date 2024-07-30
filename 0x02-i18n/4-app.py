#!/usr/bin/env python3

""" 4-app.py. Flask app and an index.html"""

from flask import Flask, render_template,request
from flask_babel import Babel


class Config:
    """ configure available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale:
    """ determine the best match with our supported languages."""
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])

app.route('/', strict_slashes=False)
def index() -> str:
    """ renders html page"""
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port: '5000', debug=True)
