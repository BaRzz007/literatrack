#!/usr/bin/env python3
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v2")

from api.v2.views.index import *
from api.v2.views.users import *
from api.v2.views.books import *
