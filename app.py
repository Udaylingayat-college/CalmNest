from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from backend.config import Config  
from backend.routes.auth_routes import auth_bp  

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)  # Enable CORS
bcrypt = Bcrypt(app)  # Initialize Bcrypt

# MongoDB Connection
client = MongoClient(app.config["MONGO_URI"])
db = client.get_database()

# Pass bcrypt instance to auth routes
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
