import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database Connection
conn = sqlite3.connect("feedback.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT,
    department TEXT,
    feedback_text TEXT
)
""")

conn.commit()

# Submit Feedback
def submit_feedback():
    name = entry_name.get()
    department = entry_department.get()
    feedback = text_feedback.get("1.0", tk.END)

    if name == "" or department == "" or feedback.strip() == "":
        messagebox.showerror("Error", "All fields are required")
        return

    cursor.execute("""
    INSERT INTO feedback (employee_name, department, feedback_text)
    VALUES (?, ?, ?)
    """, (name, department, feedback))

    conn.commit()

    messagebox.showinfo("Success", "Feedback Submitted Successfully")

    entry_name.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    text_feedback.delete("1.0", tk.END)

# GUI Window
root = tk.Tk()
root.title("Employee Feedback Tracker")
root.geometry("500x400")

# Labels
tk.Label(root, text="Employee Name").pack(pady=5)
entry_name = tk.Entry(root, width=50)
entry_name.pack()

tk.Label(root, text="Department").pack(pady=5)
entry_department = tk.Entry(root, width=50)
entry_department.pack()

tk.Label(root, text="Feedback").pack(pady=5)
text_feedback = tk.Text(root, width=50, height=10)
text_feedback.pack()

# Submit Button
submit_btn = tk.Button(root, text="Submit Feedback", command=submit_feedback)
submit_btn.pack(pady=20)

root.mainloop()
