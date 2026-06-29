import tkinter as tk 
import sqlite3
import subprocess
import sys
from config import users_db, lego_selector

def login_window(): 
    def login(): 
        
        with sqlite3.connect(users_db) as connect:
            cursor = connect.cursor()
            
            user = user_name.get()
            user_pass = user_password.get()
            
            cursor.execute(
                "Select user_id, username From users Where username = ? AND password =?", (user,user_pass,)
            )
            
            result = cursor.fetchone()
            
            if result:
                user_id = result[0]
                username = result[1]
                subprocess.Popen([sys.executable, str(lego_selector),str(user_id),username])
                window.destroy()
            else: 
                login_prompt.config(text="User Not Found")
        
    def signup():
        with sqlite3.connect(users_db) as connect:
            cursor = connect.cursor()
            
            user = user_name.get()
            user_pass = user_password.get()
            
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
    
    # Window features 
    window = tk.Tk()
    window.title("Login")
    window.geometry("600x400")
    
    user_name = tk.StringVar()
    user_password = tk.StringVar()
    
    login_prompt = tk.Label(
        window, 
        bd = 4, 
        text = "",
        font=("Arial",30)
    )
    login_prompt.pack(pady=5)
    
    user_name_entry = tk.Entry(
        window,
        textvariable= user_name, 
        bd = 4,
        font=("Arial", 30)
    )
    user_name_entry.pack(pady=5)
    
    user_password_entry = tk.Entry(
        window,
        textvariable= user_password, 
        bd = 4,
        show="*",
        font=("", 30)
    )
    user_password_entry.pack(pady=5)
    
    sign_up_button = tk.Button(
        window, 
        text = "Sign up",
        font =("Arial", 20),
        command=signup
    )
    sign_up_button.pack(pady=5)
    
    login_button = tk.Button(
        window, 
        text = "Login",
        font =("Arial", 20),
        command=login
    )
    login_button.pack(pady=5)

    window.mainloop()


if __name__ == "__main__": 
    login_window()