from procedure_manager import DatabaseManager

def insert_initial_data():
    db_manager = DatabaseManager('localhost', 'root', 'root', 'fortnite')
    db_manager.connect()


        # Insert initial updates
    db_manager.create_update('2024-01-01')
    db_manager.create_update('2024-02-01')

    # Insert initial cosmetics
    db_manager.create_cosmetic('Skin1', 10.99, 1)
    db_manager.create_cosmetic('Skin2', 15.99, 1)
    db_manager.create_cosmetic('Skin3', 12.99, 2)
    db_manager.create_cosmetic('Skin4', 20.99, 2)


    # Insert initial players
    db_manager.create_player('player1@example.com', 'password1', 1)
    db_manager.create_player('player2@example.com', 'password2', 2)
    db_manager.create_player('player3@example.com', 'password3', 1)
    db_manager.create_player('player4@example.com', 'password4', 1)


    # Insert initial weapons
    db_manager.create_weapon('Weapon1', 50, 3.5, 1)
    db_manager.create_weapon('Weapon2', 70, 4.2, 1)
    db_manager.create_weapon('Weapon3', 60, 3.8, 2)
    db_manager.create_weapon('Weapon4', 80, 4.5, 2)

    # Insert initial locations
    db_manager.create_location('Location1', 5, 1000, 10.5, 1)
    db_manager.create_location('Location2', 8, 1500, 15.2, 1)
    db_manager.create_location('Location3', 7, 1200, 12.8, 2)
    db_manager.create_location('Location4', 10, 1800, 18.5, 2)


    # Insert initial matches
    db_manager.create_match('2024-01-15', 1)
    db_manager.create_match('2024-02-15', 2)

    # Insert initial purchases
    db_manager.create_purchase(1, 1, '2024-01-02')
    db_manager.create_purchase(2, 2, '2024-01-05')

    # Insert initial friendships
    db_manager.create_friendship(1, 2)
    db_manager.create_friendship(2, 3)

    db_manager.disconnect()

if __name__ == "__main__":
    insert_initial_data()
