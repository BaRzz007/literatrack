#!/usr/bin/python3
"""
Module handles all available CRUD operations for report object
"""
from flask import jsonify, request
from models import storage
from models.report import Report
from models.user import User
from api.v1.views import app_views


@app_views.route("/users/<user_id>/reports", methods=["GET", "POST"],
        strict_slashes=False)
def get_post_reports(user_id):
    """
    GET: Returns all user's reports
    POST: Creates a new report
    """
    user = storage.get(User, user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404

    if request.method == "GET":
        reports = [report.to_dict() for report in storage.all(Report).values()
                if report.user_id == user.id]
        reports.sort(key=lambda report: report["created_at"])
        return jsonify(reports), 200

    if request.method == "POST":
        if not request.get_json():
            return jsonify({"error": "not a JSON"}), 400

        data = request.get_json()

        if "duration" not in data:
            return jsonify({"error": "duration is missing"}), 400

