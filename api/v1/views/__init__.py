#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.books import *
from api.v1.views.shelfs import *
from api.v1.views.read_sessions import *
from api.v1.views.shelfs_books import *
from api.v1.views.reviews import *
