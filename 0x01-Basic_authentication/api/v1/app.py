#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os

from api.v1.views import app_views
# Adjust import as necessary for your project structure

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize auth
auth = None
auth_type = os.getenv('AUTH_TYPE')
# check if either is the specified
if auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

# run before processing any request
@app.before_request
def before_request_handler():
    """Function to check each request before reaching secured endpoints."""
    # if auth is none, do nothing
    if auth is None:
        return

    # List of paths that do not require authentication
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    if not auth.require_auth(request.path, excluded_paths):
        return  # If path is in the excluded paths, do nothing

    if auth.authorization_header(request) is None:
        abort(401)  # If no Authorization header, raise Unauthorized error

    if auth.current_user(request) is None:
        abort(403)  # If no user could be authenticated, raise Forbidden error


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden access handler """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized access handler """
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
