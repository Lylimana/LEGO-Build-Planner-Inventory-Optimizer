import tkinter as tk 
import sqlite3

connection = sqlite3.connect(r"C:\Users\manal\Desktop\Lego Build Planner & inventory Optimizer\Lego Datasets\sets.db")

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

# User Entry
user_entered_set = tk.Entry(
    window,
    textvariable = user_set,
    bd = 4,
    justify = "center",
    font = ("Arial", 30)
)
user_entered_set.pack(pady = 5)

search_button = tk.Button(
    window,
    text="Search",
    font=("Arial",20),
    command = update_display
)
search_button.pack(pady = 20)

window.mainloop()