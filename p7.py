# Database Practice :)
import sqlite3

# Connection allows us yo connection python to a SQL database :)
connection = sqlite3.connect("./database.db") 
# From my location, target a location, connecting the python program to a SQL database

# Cursor allows us to interact with the SQL DB
cursor = connection.cursor()

query = """
SELECT product_name, price FROM Products;
"""

result = cursor.execute(query).fetchall()
print(f"Our SQL result: {result}")

# Bottom/End of our code
connection.commit() #commits our changes
connection.close() #disconnects our connection