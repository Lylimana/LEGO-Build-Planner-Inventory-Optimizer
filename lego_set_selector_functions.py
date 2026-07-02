import sqlite3
import tkinter as tk
from config import users_db, sets_db

# Helper functions 
def get_users_connection():
    return sqlite3.connect(users_db)

def get_sets_connection():
    return sqlite3.connect(sets_db)


def update_display(set_name_label, user_set): 
    set_num = user_set.get().strip()
    
    if not set_num: 
        set_name_label.config(text = "Enter a set number")
    
    with get_sets_connection() as connect: 
        cursor = connect.cursor()
    
        cursor.execute(
            "SELECT name FROM sets WHERE set_num = ?", (set_num,)   
        )

        result = cursor.fetchone()
    
    if result: 
        set_name_label.config(text=result[0])
    else: 
        set_name_label.config(text="Set not Found")
    
# Button functions
def set_to_inventory(set_name_label, user_set, user_id): 
    set_num = user_set.get().strip()
    
    if not set_num: 
        set_name_label.config(text = "Enter a set number")
        return
    
    with get_sets_connection() as connect: 
        cursor = connect.cursor()
        
        cursor.execute(
            "SELECT name From sets WHERE set_num = ?", (set_num,)
        )
        
        set_exists = cursor.fetchone()
        
        if set_exists is None: 
            set_name_label.config(text = "Set does not exist")
            return 
        
    with get_users_connection() as connect: 
        cursor = connect.cursor()
    
        cursor.execute("""
            SELECT quantity FROM owned_sets
            WHERE user_id = ? AND set_number = ?
            """,
            (user_id, set_num)               
        )
        
        owned_set = cursor.fetchone()
        
        if owned_set: 
            cursor.execute("""
                UPDATE owned_sets
                SET quantity = quantity + 1
                WHERE user_id = ? AND set_number = ?
                """,
                (user_id, set_num)               
            )
        else: 
            cursor.execute("""
                INSERT INTO owned_sets (user_id, set_number, quantity) 
                VALUES(?,?, 1)
                """,
                (user_id, set_num)               
            )
        
    set_name_label.config(text="Set Added")
    
def open_inventory(set_name_label, user_id): 
    with get_users_connection() as connect: 
        cursor = connect.cursor()
        
        cursor.execute("""
            SELECT set_number, quantity FROM owned_sets WHERE user_id = ?            
            """,
            (user_id,)
        )
    
    result = cursor.fetchall()
    
    if result: 
        inventory_window = tk.Toplevel()
        inventory_window.title("Inventory")
        inventory_window.geometry("600x400")
        
        # Table Headers 
        tk.Label(
            inventory_window, 
            text="Set Number",
            font=("Arial", 10, "bold")
        ).grid(row=0, column=0)
    
        tk.Label(
            inventory_window, 
            text="Quantity",
            font=("Arial", 10, "bold")
        ).grid(row=0, column=1)

        # Sets in table
        for i, (set_num, quantity) in enumerate(result, start = 1): 
            tk.Label(
                inventory_window, 
                text= set_num,
                font=("Arial", 10)
            ).grid(row=i, column=0)
        
            tk.Label(
                inventory_window, 
                text= quantity,
                font=("Arial", 10)
            ).grid(row=i, column=1)
            
            # Remove set
            tk.Button(
                inventory_window,
                text="Remove set",
                font=("Arial", 10)
            ).grid(row=i, column=2)
            
            # Add set
            tk.Button(
                inventory_window,
                text="Add set",
                font=("Arial", 10)
            ).grid(row=i, column=3)
    else:
        set_name_label.config(text = "You have no Sets")
