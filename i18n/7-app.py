#!/usr/bin/env python3
"""Infer appropriate time zone"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel()

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """Return user dictionary or None"""
    login_as = request.args.get('login_as')
    if login_as:
        try:
            return users.get(int(login_as))
        except (ValueError, TypeError):
            return None
    return None


@app.before_request
def before_request():
    """Find user and store it in flask.g.user"""
    g.user = get_user()


def get_locale():
    """Get locale in order of priority"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """Get timezone in order of priority"""
    tz = request.args.get('timezone')
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        user_tz = g.user.get('timezone')
        if user_tz:
            try:
                pytz.timezone(user_tz)
                return user_tz
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return "UTC"


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def index():
    """Render index page"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)