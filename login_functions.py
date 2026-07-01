import sqlite3
import subprocess
import sys
from config import users_db, lego_selector

def login(window, login_prompt, username, password):   
    with sqlite3.connect(users_db) as connect:
        cursor = connect.cursor()
        
        user = username
        
        cursor.execute(
            "Select user_id, username, password From users Where username = ?", (user,)
        )
        
        result = cursor.fetchone()
        
        if result is None:
            login_prompt.config(text="User Not Found")
        elif result[2] != password: 
            login_prompt.config(text="Password is incorrect")
        else:
            user_id = result[0]
            username = result[1]
            subprocess.Popen([sys.executable, str(lego_selector),str(user_id),username])
            window.destroy()

def signup(login_prompt, username, password):
    with sqlite3.connect(users_db) as connect:
        cursor = connect.cursor()
        
        user = username
        user_pass = password
        
        cursor.execute(
            "Select user_id, username From users Where username = ?", (user,)
        )
        
        result = cursor.fetchone()
        
        if result: 
            login_prompt.config(text="User Already Exists")
        else: 
            cursor.execute("""
                INSERT INTO users (username, password)
                VALUES (?,?)
                """,
                (user, user_pass)
            )
            login_prompt.config(text="User Created")
            connect.commit()

