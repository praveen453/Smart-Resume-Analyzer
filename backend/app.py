from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# Database connection
db_config = {
    "host": "localhost",
    "user": "root",  # Change this
    "password": "",  # Change this
    "database": "resume_analyzer"  # Change this
}

def connect_db():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None

# Test route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to Smart Resume Analyzer API!"})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
