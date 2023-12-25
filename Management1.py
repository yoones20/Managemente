import sqlite3

conn = sqlite3.connect("example.db")


cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teacher(
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Number_class INTEGER,
        Time_class INTEGER
 )              
""") 

cursor.execute("""
CREATE TABLE  IF NOT EXISTS honar_amoz(
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Number_class INEGER,
        Nomre INTEGER
)
""")


conn.commit()

conn.close()