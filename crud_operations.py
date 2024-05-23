import mysql.connector
from procedure_manager import DatabaseManager  # Import the DatabaseManager

def main():
    db = DatabaseManager('localhost', 'root', 'root', 'fortnite')
    db.connect()

    # Inserting data into tables
    insert_initial_data(db)

    # Performing CRUD operations
    perform_crud_operations(db)

    db.disconnect()

def insert_initial_data(db_manager):
    # Inserting initial data into each table
    cosmetics = [
        ("Raven Outfit", "Outfit", 2000.00),
        ("Iron Cage", "Back Bling", 1500.00),
        ("Bitemark", "Pickaxe", 1200.00),
        ("Feathered Flyer", "Glider", 800.00),
        ("Reaper", "Pickaxe", 800.00)
    ]
    for cosmetic in cosmetics:
        db_manager.create_cosmetic(*cosmetic)

    players = [
        ("password123", 1),
        ("password234", 2),
        ("password345", 3),
        ("password456", 4),
        ("password567", 5)
    ]
    for player in players:
        db_manager.create_player(*player)

    weapons = [
        (95, 0.80),
        (75, 1.75),
        (33, 9.0),
        (110, 1.0),
        (150, 0.33)
    ]
    for weapon in weapons:
        db_manager.create_weapon(*weapon)

    locations = [
        (5, 500, 0.5),
        (10, 1000, 1.0),
        (3, 300, 1.5),
        (8, 800, 2.0),
        (7, 700, 2.5)
    ]
    for location in locations:
        db_manager.create_location(*location)

    updates = [
        ("Tilted Towers, Haunted Hills", "Rocket Launcher", "Ninja Outfit", "Daily", "Yes", "No", "2021-01-01"),
        ("Dusty Depot, Pleasant Park", "Golden Axe", "Reaper", "Weekly", "No", "Yes", "2021-01-15"),
        ("Haunted Hills, Dusty Depot", "Pump Shotgun", "Iron Cage", "Monthly", "Yes", "Yes", "2021-02-01")
    ]
    for update in updates:
        db_manager.create_update(*update)

    plays = [
        (1, 1, 1, 5, 10),
        (2, 2, 2, 3, 5),
        (3, 3, 3, 7, 15),
        (4, 4, 4, 2, 3),
        (5, 5, 5, 1, 1)
    ]
    for play in plays:
        db_manager.create_play(*play)

    matches = [
        (1, 1, "2021-01-01"),
        (2, 2, "2021-01-15"),
        (3, 3, "2021-02-01")
    ]
    for match in matches:
        db_manager.create_match(*match)

    purchases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    for purchase in purchases:
        db_manager.create_purchase(*purchase)

    friends = [
        (1, 2),
        (1, 3),
        (4, 5)
    ]
    for friend in friends:
        db_manager.create_friend(*friend)

    print("Initial data inserted successfully.")

def perform_crud_operations(db_manager):
    # Example CRUD operations
    
    # Update a player's password
    db_manager.update_player(1, 'newpassword999', 1)

    # Fetch and print all players
    print("Players:")
    players = db_manager.get_players()
    for player in players:
        print(player)

    # Delete a cosmetic
    db_manager.delete_cosmetic(5)

    # Fetch and print all cosmetics
    print("Cosmetics:")
    cosmetics = db_manager.get_cosmetics()
    for cosmetic in cosmetics:
        print(cosmetic)

    # Add other CRUD operations similarly...

if __name__ == "__main__":
    main()
