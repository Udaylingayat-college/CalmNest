from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
import jwt
import datetime
from backend.config import Config
from backend.models import users_collection
from flask_bcrypt import Bcrypt

auth_bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()  # Define bcrypt instance

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    if users_collection.find_one({"email": email}):
        return jsonify({"message": "User already exists"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = {
        "name": name,
        "email": email,
        "password": hashed_password,
        "created_at": datetime.datetime.utcnow()
    }
    users_collection.insert_one(new_user)

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = users_collection.find_one({"email": data["email"]})

    if not user:
        return jsonify({"message": "User not found"}), 404

    if not bcrypt.check_password_hash(user["password"], data["password"]):
        return jsonify({"message": "Invalid credentials"}), 401

    # Debug prints
    print("User found:", user)  # See what user object contains
    print("SECRET_KEY:", Config.SECRET_KEY)  # Check if SECRET_KEY exists

    token = jwt.encode(
        {"email": user["email"], "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)}, 
        Config.SECRET_KEY, 
        algorithm="HS256"
    )

    return jsonify({"token": token})




