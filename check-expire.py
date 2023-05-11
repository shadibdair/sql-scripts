# import sqlite3
# from datetime import datetime

# # Connect to the SQLite database
# conn = sqlite3.connect('my_database.db')
# c = conn.cursor()

# # Query the 'products' table
# c.execute("SELECT product_id, expiration_date FROM products;")
# data = c.fetchall()

# # Get current date
# current_date = datetime.now()
# current_date_str = current_date.strftime('%d/%m/%Y')
# current_date = datetime.strptime(current_date_str, '%d/%m/%Y')

# # Check each product for expiration
# for row in data:
#     product_id, expiration_date = row
#     expiration_date = datetime.strptime(expiration_date, '%d/%m/%Y')

#     if expiration_date < current_date:
#         print(f'Product ID {product_id} is expired.')

# # Close the connection
# conn.close()

import sqlite3
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('/Users/shadibadir/Desktop/hackathon-tsofen-2023/sql-json/my_database.db')
c = conn.cursor()

# Query the 'products' table
c.execute("SELECT name, expiration_date FROM products;")
data = c.fetchall()

# Get current date and the date for one week later
current_date = datetime.now()
one_week_later = current_date + timedelta(weeks=1)

# Convert dates to string and then back to date to get rid of time
current_date_str = current_date.strftime('%d/%m/%Y')
one_week_later_str = one_week_later.strftime('%d/%m/%Y')

current_date = datetime.strptime(current_date_str, '%d/%m/%Y')
one_week_later = datetime.strptime(one_week_later_str, '%d/%m/%Y')

# Check each product for expiration
for row in data:
    name, expiration_date = row
    expiration_date = datetime.strptime(expiration_date, '%d/%m/%Y')

    if current_date <= expiration_date < one_week_later:
        print(f'Product Name : {name} will expire within one week.')

# Close the connection
conn.close()
