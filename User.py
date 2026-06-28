import sqlite3
from config import users_db

def create_database():
    with sqlite3.connect(users_db) as connect:
        cursor = connect.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        # Helps automatically close connection compared to doing it manually line 10, 39 and 40

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL 
    )
    """
    )
    # In Future store do not store passwords as plain text - use hashlib/bcrypt

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS owned_sets (
        owned_set_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        set_number TEXT NOT NULL,
        quantity INTEGER DEFAULT 1,
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        UNIQUE(user_id, set_number)
        )
    """
    )

    # connect.commit()
    # connect.close()

if __name__ == "__main__":
    create_database()

