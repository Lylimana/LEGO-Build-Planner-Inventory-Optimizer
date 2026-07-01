import tkinter as tk 
import sys
from lego_set_selector_functions import update_display, set_to_inventory, open_inventory

def lego_selector_window():
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
        command = lambda: update_display(set_name_label, user_set)
    )
    search_button.pack(pady = 20)

    add_set_button = tk.Button(
        window,
        bd= 4,
        text="Add set to Inventory",
        font=("Arial", 20),
        command= lambda: set_to_inventory(set_name_label, user_set, user_id)
    )
    add_set_button.pack(pady = 5)

    inventory = tk.Button(
        window,
        bd= 4,
        text="Inventory",
        font=("Arial", 20),
        command= lambda: open_inventory(set_name_label, user_id)
    )
    inventory.pack(pady = 5)

    window.bind("<Return>", lambda event: update_display(set_name_label, user_set))
    
    window.mainloop()

    
if __name__ == "__main__": 
    lego_selector_window()