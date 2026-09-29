import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

def create_user(username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    try:
        password_hash = generate_password_hash(password)

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password_hash)
        )

        connection.commit()
        return True

    except sqlite3.IntegrityError:
        return False
    
    finally:
        connection.close()