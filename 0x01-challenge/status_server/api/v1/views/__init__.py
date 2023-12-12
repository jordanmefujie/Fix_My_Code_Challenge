#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
