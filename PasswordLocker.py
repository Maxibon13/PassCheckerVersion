import os
import urllib.request

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def Verify():
    global current_file_path, parent_directory_path
    file_path = os.path.abspath(__file__)

    # Check git-repo
    with open(file_path, "r") as file:
        local_content = file.read()

    # Download the main file from the Git repository
    response = urllib.request.urlopen("https://raw.githubusercontent.com/Maxibon13/PassCheckerVersion/main/PasswordLocker.py")
    _git_content = response.read().decode('utf-8')

    print(_git_content, local_content)
    
    if _git_content == local_content:
        locked_ui()
    else:
        return

def check_password():
    entered_password = password_entry.get()
    if entered_password == "pass":
        locked_window.withdraw()
        unlock_ui()
    else:
        messagebox.showerror("Error", "Invalid password!")

def unlock_ui():
    global unlocked_window 

    unlocked_window = tk.Toplevel()
    unlocked_window.title("Vault")
    unlocked_window.geometry("350x250")

    unlocked_window.resizable(False, False)

    unlocked_label = ttk.Label(unlocked_window, text="Unlocked!", font=("Helvetica", 16))
    unlocked_label.pack(pady=50)

    close_button = ttk.Button(unlocked_window, text="Close", command=unlocked_window.destroy)
    close_button.pack(pady=20)

    unlocked_window.mainloop()

def locked_ui():   
    global locked_window, password_entry 

    locked_window = tk.Toplevel()
    locked_window.geometry("350x250")
    locked_window.title("Locked")

    locked_window.resizable(False, False)

    # Password label
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 16))

    key_label = ttk.Label(locked_window, text="Key:", style="TLabel")
    key_label.place(x=50, y=85)

    # Password field
    style.configure("TEntry", font=("Helvetica", 16), padding=5, relief="solid")

    password_entry = ttk.Entry(locked_window, show="*", style="TEntry")
    password_entry.place(x=115, y=85)

    # Check button
    style.configure("TButton", relief="raised", font=("Helvetica", 20), padding=10, borderwidth=2, foreground="black")
    style.map("TButton", foreground=[('pressed', 'red'), ('active', 'blue')])

    check_button = ttk.Button(locked_window, text="Check", style="TButton", command=check_password)
    check_button.place(x=85, y=140)

    locked_window.mainloop()

# Create the root window
root = tk.Tk()
root.withdraw()
Verify()
