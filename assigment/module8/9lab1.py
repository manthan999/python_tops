import sqlite3

# 1. Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("students.db")

# 2. Create a cursor object
cursor = conn.cursor()

# 3. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

# 4. Insert data into table
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("Alice", 20))
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("Bob", 22))
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("Charlie", 21))

# Save (commit) changes
conn.commit()

# 5. Fetch data
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

# 6. Display data
print("Student Records:")
for row in rows:
    print(row)

# 7. Close the connection
conn.close()
