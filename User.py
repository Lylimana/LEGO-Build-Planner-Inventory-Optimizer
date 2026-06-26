import sqlite3
import os


def create_database():
    base_folder = r"C:\Users\manal\Desktop\Lego Build Planner & inventory Optimizer\Lego Datasets"

    db_path = os.path.join(base_folder, "Users.db")

    connect = sqlite3.connect(db_path)

    cursor = connect.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

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



    connect.commit()
    connect.close()

if __name__ == "__main__":
    create_database()

