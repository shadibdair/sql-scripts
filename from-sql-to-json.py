import json
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# Query the 'users' table
c.execute('SELECT * FROM users')
data = c.fetchall()

# Convert the query results to a list of dictionaries
# Note: Adjust the field names if your database schema is different
data = [dict(id=row[0], name=row[1], email=row[2]) for row in data]

# Write the data to a JSON file
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)

# Close the connection
conn.close()
