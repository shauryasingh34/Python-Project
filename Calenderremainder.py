import tkinter as tk
from tkinter import messagebox
import calendar
import datetime
import pickle
import os

REMINDER_FILE = "reminders.pkl"

def load_reminders():
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "rb") as f:
            return pickle.load(f)
    return {}

def save_reminders():
    with open(REMINDER_FILE, "wb") as f:
        pickle.dump(reminders, f)

def show_calendar():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())
        cal = calendar.month(year, month)
        cal_text.config(state="normal")
        cal_text.delete("1.0", tk.END)
        cal_text.insert(tk.END, cal)
        cal_text.config(state="disabled")
    except:
        messagebox.showerror("Invalid Input", "Enter valid year and month")

def add_reminder():
    date = date_entry.get()
    note = note_entry.get()
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except:
        messagebox.showerror("Date Error", "Use YYYY-MM-DD format")
        return
    if note.strip():
        reminders[date] = note
        save_reminders()
        messagebox.showinfo("Saved", f"Reminder saved for {date}")
        note_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty", "Reminder cannot be empty")

def check_today():
    today = datetime.date.today().isoformat()
    if today in reminders:
        messagebox.showinfo("Today's Reminder", f"{today}: {reminders[today]}")

reminders = load_reminders()
root = tk.Tk()
root.title("🗓 Calendar & Reminder")
root.geometry("430x600")
root.config(bg="#f0f0f5")

title = tk.Label(root, text="📅 Calendar & Reminder App", font=("Helvetica", 16, "bold"), bg="#f0f0f5", fg="#2e3f4f")
title.pack(pady=10)

frame_input = tk.Frame(root, bg="#f0f0f5")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Year:", bg="#f0f0f5", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)
year_entry = tk.Entry(frame_input, width=8)
year_entry.insert(0, datetime.datetime.now().year)
year_entry.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Month:", bg="#f0f0f5", font=("Helvetica", 12)).grid(row=0, column=2, padx=5)
month_entry = tk.Entry(frame_input, width=4)
month_entry.insert(0, datetime.datetime.now().month)
month_entry.grid(row=0, column=3, padx=5)

tk.Button(frame_input, text="Show Calendar", command=show_calendar, bg="#4caf50", fg="white", width=15).grid(row=1, column=0, columnspan=4, pady=10)

cal_text = tk.Text(root, height=10, width=32, font=("Courier", 12), state="disabled", bg="white")
cal_text.pack(pady=10)

tk.Label(root, text="📝 Add Reminder", font=("Helvetica", 14, "bold"), bg="#f0f0f5", fg="#2e3f4f").pack(pady=5)

frame_reminder = tk.Frame(root, bg="#f0f0f5")
frame_reminder.pack()

tk.Label(frame_reminder, text="Date (YYYY-MM-DD):", bg="#f0f0f5").grid(row=0, column=0, padx=5, pady=5, sticky='e')
date_entry = tk.Entry(frame_reminder, width=15)
date_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_reminder, text="Reminder:", bg="#f0f0f5").grid(row=1, column=0, padx=5, pady=5, sticky='e')
note_entry = tk.Entry(frame_reminder, width=30)
note_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="➕ Add Reminder", command=add_reminder, bg="#2196f3", fg="white", width=20).pack(pady=10)

tk.Button(root, text="📌 Check Today's Reminder", command=check_today, bg="#ff5722", fg="white", width=25).pack(pady=5)

check_today()

root.mainloop()
