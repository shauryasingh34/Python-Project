import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4.")
            return

        characters = ''
        if use_upper.get():
            characters += string.ascii_uppercase
        if use_lower.get():
            characters += string.ascii_lowercase
        if use_digits.get():
            characters += string.digits
        if use_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_output.delete(0, tk.END)
        password_output.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    password = password_output.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x400")
root.config(bg="#f0f4f8")
root.resizable(False, False)

tk.Label(root, text="Password Generator", font=("Helvetica", 20, "bold"), bg="#f0f4f8", fg="#333").pack(pady=20)

tk.Label(root, text="Password Length:", bg="#f0f4f8", font=("Helvetica", 12)).pack()
length_entry = tk.Entry(root, font=("Helvetica", 12), width=10, justify="center")
length_entry.pack(pady=5)

use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=use_upper, bg="#f0f4f8").pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=use_lower, bg="#f0f4f8").pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Numbers", variable=use_digits, bg="#f0f4f8").pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols, bg="#f0f4f8").pack(anchor='w', padx=40)

tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=20).pack(pady=15)

password_output = tk.Entry(root, font=("Courier", 14), width=28, justify="center")
password_output.pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white", font=("Helvetica", 12), width=20).pack(pady=5)

tk.Label(root, text="Made with ❤️ in Python", bg="#f0f4f8", fg="#888", font=("Arial", 10)).pack(side="bottom", pady=10)

root.mainloop()
