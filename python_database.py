import sqlite3

# Query the database and return all records


def show_all():

    conn = sqlite3.connect('second.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()

# Add a new record to the table


def add_one(first, last, email):
    conn = sqlite3.connect('second.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    conn.commit()
    conn.close()

# Add many records


def add_many(list):
    conn = sqlite3.connect('second.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

# Delete a records from table


def delete_one(id):
    conn = sqlite3.connect('second.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

# Lookup with Where


def email_lookup(email):
    conn = sqlite3.connect('second.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()
