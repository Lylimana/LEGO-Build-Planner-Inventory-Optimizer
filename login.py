import tkinter as tk 
from login_functions import login, signup

def login_window():  
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
    
    # Buttons 
    sign_up_button = tk.Button(
        window, 
        text = "Sign up",
        font =("Arial", 20),
        command=lambda: signup(login_prompt, 
                               user_name.get(), 
                               user_password.get())
    )
    sign_up_button.pack(pady=5)
    
    login_button = tk.Button(
        window, 
        text = "Login",
        font =("Arial", 20),
        command=lambda: login(window, 
                              login_prompt, 
                              user_name.get(), 
                              user_password.get())
    )
    login_button.pack(pady=5)
    
    window.bind("<Return>", lambda event: login(window, 
                                                login_prompt, 
                                                user_name.get(), 
                                                user_password.get()))

    window.mainloop()


if __name__ == "__main__": 
    login_window()