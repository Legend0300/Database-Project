import mysql.connector
from Faker import DatabaseFaker
from procedure_manager import DatabaseManager  # Assuming you have defined this class

# Connect to the database using the DatabaseManager
db_manager = DatabaseManager('localhost', 'root', 'root', 'fortnite')
db_manager.connect()

# Initialize the DatabaseFaker with the DatabaseManager
faker = DatabaseFaker(db_manager)

#  Generate 100 players
# faker.create_player(1000)

# Generate 10 matches
faker.create_matches(10)
    


# Disconnect from the database
db_manager.disconnect()
