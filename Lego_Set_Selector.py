import tkinter as tk 
import sqlite3
import sys
from config import users_db, sets_db

connection = sqlite3.connect(sets_db)

cursor = connection.cursor()

# Display   
window = tk.Tk()
window.title("Lego Set Selector")
window.geometry("600x350")

# Storing User input
user_set = tk.StringVar()

# Label to display result
set_name_label = tk.Label(
    window,
    text = "Enter Set Number",
    font = ("Arial", 30)
)
set_name_label.pack(pady = 5)

# Update display
def update_display(): 
    set_num = user_set.get()
    
    cursor.execute(
        "SELECT name FROM sets WHERE set_num = ?", (set_num,)   
    )

    result = cursor.fetchone()
    
    if result: 
        set_name_label.config(text=result[0])
    else: 
        set_name_label.config(text="Set not Found")

def set_to_inventory(): 
    set_num = user_set.get()
    user_id = int(sys.argv[1])
    
    with sqlite3.connect(users_db) as connect: 
        cursor = connect.cursor()
    
    cursor.execute("""
        INSERT INTO owned_sets (user_id, set_number) 
        VALUES(?,?)
        """,
        (user_id, set_num)               
    )
    
    set_name_label.config(text="Set Added")

# User Entry
user_entered_set = tk.Entry(
    window,
    textvariable = user_set,
    bd = 4,
    justify = "center",
    font = ("Arial", 30)
)
user_entered_set.pack(pady = 5)

# Buttons
search_button = tk.Button(
    window,
    text="Search",
    font=("Arial",20),
    command = update_display
)
search_button.pack(pady = 20)

add_set_button = tk.Button(
    window,
    bd= 4,
    text="Add set to Inventory",
    font=("Arial", 20),
    command= set_to_inventory
)
add_set_button.pack(pady = 5)

window.bind("<Return>", lambda event: update_display())

window.mainloop()