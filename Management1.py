import sqlite3

conn = sqlite3.connect("example.db")


cursor = conn.cursor

cursor.execute("""
CREAT TABLE IF NOT EXISTS teacher,
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        number_class INTEGER,
        time_class INTEGER,
""")