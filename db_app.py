import database

# # Add record to DB
# database.add_one("Gary", "Tester", "gg@souls.com")

# # Add many records to DB
# database.add_many_random(10)

# # Delete record at rowid
# database.delete_one("1")

# # Add Many records
# stuff = [
#     ('Way', 'Out', 'wocause@tiscali.com'),
#     ('Mona', 'Shisha', 'misha@kek.com')
# ]
# database.add_many(stuff)

# DB email lookup
database.email_lookup("timothyjensen@jensen.com")

# # Show all in DB
# database.show_all()