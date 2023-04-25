#!/usr/bin/env python3
""" Module for Babel i18n """
from flask_babel import Babel, _
from flask import Flask, render_template, request, flash

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ Configuration Class for Babel """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Select a language translation request"""
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def get_index() -> str:
    """Renders Basic template
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
