import mysql.connector

# Database connection details
db_config = {
    "host": "localhost",
    "user": "root",  # Change this
    "password": "",  # Change this
    "database": "resume_analyzer"  # Change this
}

def connect_db():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("✅ Connected to MySQL Database!")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None

# Test connection
if __name__ == "__main__":
    connect_db()
