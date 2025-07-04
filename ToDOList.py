import tkinter as tk
from tkinter import messagebox, ttk

tasks = []

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_all():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
        tasks.clear()
        update_listbox()

def update_listbox():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        task_listbox.insert(tk.END, f"{i}. {task}")

# ----- GUI Setup -----
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x500")
root.config(bg="#F7F7F7")
root.resizable(False, False)

# ----- Header -----
title = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#F7F7F7", fg="#333")
title.pack(pady=15)

# ----- Entry Box -----
task_entry = tk.Entry(root, font=("Helvetica", 12), width=28, bd=2, relief="solid")
task_entry.pack(pady=10)

# ----- Button Frame -----
button_frame = tk.Frame(root, bg="#F7F7F7")
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Task", command=add_task, bg="#4CAF50", fg="white", width=10)
add_btn.grid(row=0, column=0, padx=5)

del_btn = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#F44336", fg="white", width=10)
del_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(button_frame, text="Clear All", command=clear_all, bg="#9E9E9E", fg="white", width=10)
clear_btn.grid(row=0, column=2, padx=5)

# ----- Task Listbox with Scrollbar -----
frame_list = tk.Frame(root)
frame_list.pack(pady=10)

scrollbar = tk.Scrollbar(frame_list, orient=tk.VERTICAL)
task_listbox = tk.Listbox(
    frame_list,
    width=45,
    height=15,
    font=("Courier New", 12),
    yscrollcommand=scrollbar.set,
    bd=2,
    relief="solid",
    selectbackground="#D1C4E9",
    selectforeground="#000"
)
scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.pack()

# ----- Footer -----
footer = tk.Label(root, text="Made with ❤️ in Python", bg="#F7F7F7", fg="#777", font=("Arial", 10))
footer.pack(pady=15)

root.mainloop()
