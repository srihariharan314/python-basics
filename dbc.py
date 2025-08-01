import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER)''')

# Insert data
cursor.execute("INSERT INTO student (name, marks) VALUES (?, ?)", ("G.Sri Hariharan", 90))

# Fetch data
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Commit and close
conn.commit()
conn.close()
