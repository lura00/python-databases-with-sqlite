# import sqlite3

datatypes in SQLite
NULL - om något existerar eller ej
iNTEGER - Heltal
REAL - Decimaltal
TEXT - är text
BLOB - t.ex bilder, mp3-filer

# create memory
#conn = sqlite3.connect(':memory:')

# initilize database (connecting)
conn = sqlite3.connect('second.db')

# create a cursor
c = conn.cursor()

# note: If you create functions you need to initilize and create cursor in every function

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

# create a table
 c.execute("""CREATE TABLE customers (
     first_name text,
     last_name text,
     email text
 )""")

# Add more info at once
 many_customers = [('John', 'Mayer', 'john@mayer.com'), 
                   ('Carola', 'Häggqvist', 'carola@gmail.com'), 
                   ('Bruce', 'Springsteen', 'bruce@gmail.com'),
                   ('Wes', 'Andersen', 'wes@mayer.com'), 
                   ('Wesley', 'Snipes', 'wesley@gmail.com'), 
                   ('Stefan', 'Löfven', 'stefan@gmail.com')
                  ]

# Adding one item to table
 c.execute("INSERT INTO customers VAUES('first_name', 'last_name', 'email')")

# How to search / filter in a table use WHERE
 c.execute("SELECT * FROM customers WHERE last_name = 'Elder'")

# Update records - Needs commmit
 c.execute("""UPDATE customers SET first_name = 'Marty'
 WHERE rowid = 2
 """)
 conn.commit()

# Delete records - needs to be commit
 c.execute("DELETE from customers WHERE rowid = 3")
 conn.commit()

# Order by
# low to high: rowid ASC (but it is default)
# high to low: rowid DESC
# By any lite in your table, example last_name
 c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

# Query the database - AND/OR
 c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR first_name LIKE 'Br%'")

# Limit - Limit the output
 c.execute("SELECT rowid, * FROM customers LIMIT 4")

# Delete a table - needs to be commit.
 c.execute("DROP TABLE customers")
 conn.commit()

# When adding more than one info
 c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
 c.execute("SELECT rowid, * FROM customers")
 c.fetchone()
 c.fetchmany(3)
 c.fetchall()
 items = c.fetchall()

# Looping through our file and printing it
 for item in items:
     print(item)


# For loop through table for nicer output (example)
 print("NAME \t\t| " + "\tEMAIL")
 print("--------" + "\t\t---------")
 for item in items:
     print(item[0] + "  " + item[1] + "\t\t" + item[2])

# print("\nCommand executet successfully!")
# Commit our command
 conn.commit()

# Close our connection
 conn.close()