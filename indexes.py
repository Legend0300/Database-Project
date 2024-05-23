import mysql.connector
def create_indexes():
    # Connect to MySQL
    mydb = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='fortnite'
    )
    # Create cursor
    cursor = mydb.cursor()
    # Index creation queries
    queries = [
    "CREATE INDEX idx_password ON Player(password);",
    "CREATE INDEX idx_currently_equipped ON Player(currently_equipped);",

    "CREATE INDEX idx_cosmetic_type ON Cosmetics(cosmetic_type);",
    "CREATE INDEX idx_price ON Cosmetics(price);",
    "CREATE INDEX idx_damage ON Weapon(damage);",
    "CREATE INDEX idx_fire_rate ON Weapon(fire_rate);",
    "CREATE INDEX idx_weapons_available ON Location(weapons_available);",
    "CREATE INDEX idx_material_available ON Location(material_available);",
    "CREATE INDEX idx_enemies_killed ON Play(enemies_killed);",
    "CREATE INDEX idx_time_played ON Play(time_played);",
    "CREATE INDEX idx_date_played ON `Match`(date_played);",
    "CREATE INDEX idx_cosmetic_id ON Purchase(cosmetic_id);",
    "CREATE INDEX idx_player_id_2 ON Friends(player_id_2);"
    ]
    # Execute queries
    for query in queries:
        try:
            cursor.execute(query)
            print(f"Executed: {query}")
        except mysql.connector.Error as err:
            print(f"Error: {err.msg}")
    # Commit changes
    mydb.commit()
    # Close connection
    cursor.close()
    mydb.close()
if __name__ == "__main__":
    create_indexes()