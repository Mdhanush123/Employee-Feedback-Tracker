import sqlite3

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
conn.close()

print("Database Created Successfully")
