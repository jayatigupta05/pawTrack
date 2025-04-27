import sqlite3

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect('pet_care.db')
c = conn.cursor()

# Create the pets table
c.execute('''
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        breed TEXT,
        age INTEGER,
        gender TEXT,
        vaccination_status TEXT
    )
''')

conn.commit()
conn.close()

print("Pets table created successfully!")