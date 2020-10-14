import sqlite3
import names


# Query the DB and return all records
def show_all():
    # Connect to a database and create curson
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    # Query the database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command and close connection
    conn.commit()
    conn.close()

# Add a new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    # Commit our command and close connection
    conn.commit()
    conn.close()


# Add many records to the table
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    # Commit our command and close connection
    conn.commit()
    conn.close()


# Add randomly generated records
def add_many_random(num):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    many_customers = []
    for i in range(num):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        email = f"{first_name}{last_name}@{last_name}.com".lower()
        record = (first_name, last_name, email)
        many_customers.append(record)

    c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

    # Commit our command and close connection
    conn.commit()
    conn.close()


# Delete record from table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)

    # Commit our command and close connection
    conn.commit()
    conn.close()


# Lookup with Where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command and close connection
    conn.commit()
    conn.close()


# Create a table
# # Datatypes: NULL, INTEGER, REAL, TEXT, BLOB
# c.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
#     )""")

# # Query the Database - ORDER BY
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

# # Query the Database - AND/OR
# c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE 'Joh%' OR rowid = 4")

# # Query the Database - LIMIT
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")

# # Drop Table
# c.execute("DROP TABLE customers")

# # print(c.fetchone()[0])

# Get a print in console that something happened
print("Done")

