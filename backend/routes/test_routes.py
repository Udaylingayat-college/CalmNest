from flask import Blueprint, request, jsonify
from models import tests_collection
from datetime import datetime


test_bp = Blueprint("test", __name__)

@test_bp.route("/submit-test", methods=["POST"])
def submit_test():
    data = request.json
    score = sum([q["score"] for q in data["answers"]])

    result = {
        "email": data["email"],
        "score": score,
        "timestamp": datetime.datetime.utcnow()
    }

    tests_collection.insert_one(result)
    return jsonify({"message": "Test submitted successfully", "score": score})
