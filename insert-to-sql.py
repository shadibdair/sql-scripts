import json
import sqlite3

# Load JSON data
with open('data.json') as f:
    data = json.load(f)

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# Create a new table named 'products'
c.execute('''
    CREATE TABLE products (
        product_id TEXT PRIMARY KEY,
        name TEXT,
        user_email TEXT,
        start_date TEXT,
        expiration_date TEXT,
        amount INTEGER
    )
''')

# Insert JSON data into the 'products' table
for item in data:
    c.execute('''
        INSERT INTO products (product_id, name, user_email, start_date, expiration_date, amount)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (item['product_id'], item['name'], item['user_email'], item['start_date'], item['expiration_date'], item['amount']))

# Commit the transaction and close the connection
conn.commit()
conn.close()
