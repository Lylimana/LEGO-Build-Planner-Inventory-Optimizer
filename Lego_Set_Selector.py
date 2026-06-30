import tkinter as tk 
import sqlite3
import sys
from config import users_db, sets_db

def lego_selector_window():
    connection = sqlite3.connect(sets_db)

    cursor = connection.cursor()

    # Display   
    window = tk.Tk()
    window.title("Lego Set Selector")
    window.geometry("600x400")

    # User ID 
    user_id = int(sys.argv[1])

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
        
        with sqlite3.connect(users_db) as connect: 
            cursor = connect.cursor()
        
            cursor.execute("""
                SELECT quantity FROM owned_sets
                WHERE user_id = ? AND set_number = ?
                """,
                (user_id, set_num)               
            )
            
            result = cursor.fetchone()
            
            if result: 
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
        
    def open_inventory(): 
        with sqlite3.connect(users_db) as connect: 
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
        else:
            set_name_label.config(text = "You have no Sets")


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

    inventory = tk.Button(
        window,
        bd= 4,
        text="Inventory",
        font=("Arial", 20),
        command= open_inventory
    )
    inventory.pack(pady = 5)

    window.bind("<Return>", lambda event: update_display())

    window.mainloop()
    connection.close()
    
if __name__ == "__main__": 
    lego_selector_window()