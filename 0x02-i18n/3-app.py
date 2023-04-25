#!/usr/bin/env python3
""" Module for Babel i18n
"""
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ Configuration Class for Babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """ Select a language translation
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """ Renders a Basic Template
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
