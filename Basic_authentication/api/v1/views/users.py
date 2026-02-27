#!/usr/bin/env python3
"""Module of User views"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_users():
    """GET /api/v1/users - list all users"""
    users = User.all()
    return jsonify([u.to_dict() for u in users])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """GET /api/v1/users/:id - get one user"""
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """DELETE /api/v1/users/:id"""
    user = User.get(user_id)
    if user is None:
        abort(404)
    User.remove(user_id)
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """POST /api/v1/users - create user (email, password, first_name, last_name)"""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    email = data.get("email")
    if not email:
        return jsonify({"error": "Missing email"}), 400
    password = data.get("password")
    if not password:
        return jsonify({"error": "Missing password"}), 400
    if User.find_by(email=email):
        return jsonify({"error": "User already exists for this email"}), 400
    user = User.create(
        email=email,
        password=password,
        first_name=data.get("first_name", ""),
        last_name=data.get("last_name", "")
    )
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """PUT /api/v1/users/:id - update first_name, last_name"""
    user = User.get(user_id)
    if user is None:
        abort(404)
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    user = User.update(
        user_id,
        first_name=data.get("first_name", user.first_name),
        last_name=data.get("last_name", user.last_name)
    )
    return jsonify(user.to_dict()), 200
