#!/usr/bin/env python3
"""Flask application for user authentication (registration, sessions, profile).
"""
import flask
from flask import Flask, jsonify, redirect, request

from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Root route."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """Register a user from form fields email and password.

    On success: JSON with email and message "user created", status 200.
    If email exists: JSON message "email already registered", status 400.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email=email, password=password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """POST /sessions: form fields email and password.

    On invalid credentials: flask.abort(401). On success: JSON with email and
    message "logged in", Set-Cookie session_id=..., Path=/, status 200.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email=email, password=password):
        flask.abort(401)
    session_id = AUTH.create_session(email=email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id, path="/")
    return response, 200


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """DELETE /sessions: session_id cookie; destroy session or 403.

    Read session_id from cookies, find user via AUTH.get_user_from_session_id.
    If no user: flask.abort(403). Else AUTH.destroy_session, redirect to GET
    / with status 302 and clear the session_id cookie.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id=session_id)
    if user is None:
        flask.abort(403)
    AUTH.destroy_session(user_id=user.id)
    response = redirect("/", code=302)
    response.delete_cookie("session_id", path="/")
    return response, 302


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """GET /profile: read session_id cookie, resolve user via AUTH.

    Valid session: JSON {"email": "<user email>"} with status 200.
    Missing/invalid session or unknown user: flask.abort(403).
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id=session_id)
    if user is None:
        flask.abort(403)
    payload = jsonify({"email": user.email})
    return payload, 200


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    """POST /reset_password: form field email.

    Unknown email: flask.abort(403). Else 200 and JSON email, reset_token.
    """
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email=email)
    except ValueError:
        flask.abort(403)
    body = jsonify({"email": email, "reset_token": reset_token})
    return body, 200


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password():
    """PUT /reset_password: form fields email, reset_token, new_password.

    On ValueError (invalid token): flask.abort(403). Else 200 and JSON with
    the submitted email and message "Password updated".
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        flask.abort(403)
    return jsonify(
        {"email": email, "message": "Password updated"}
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
