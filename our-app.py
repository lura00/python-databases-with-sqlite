import python_database

# Add a record to the database
#python_database.add_one("Tiger", "Woods", "tiger@gmail.com")

# Delete a record from the db, u need to use rowid as String
# python_database.delete_one('6')

# Add many records
# stuff = [('James', 'Bond', 'james@bond.com'),
#          ('Sergio', 'Ramos', 'sergio@gmail.com')
#          ]
# python_database.add_many(stuff)

# Lookup Email adress record
python_database.email_lookup("james@bond.com")

# Show all the records
python_database.show_all()
