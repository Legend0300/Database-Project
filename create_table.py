import mysql.connector
# Connect to MySQL
mydb = mysql.connector.connect(
user='root',
password='root',
host='localhost',
database='fortnite')
# Create cursor
cursor = mydb.cursor()
# Execute MySQL queries to create tables
# Creating tables in correct order and defining foreign keys after necessarytables exist
queries = [
"""CREATE TABLE Cosmetics (
cosmetic_id INT AUTO_INCREMENT PRIMARY KEY,
cosmetic_name VARCHAR(255),
cosmetic_type VARCHAR(255),

price DECIMAL(10, 2)
)""",
"""CREATE TABLE Player (
id INT AUTO_INCREMENT PRIMARY KEY,
password VARCHAR(255),
currently_equipped INT,
FOREIGN KEY (currently_equipped) REFERENCES Cosmetics(cosmetic_id)
)""",
"""CREATE TABLE Weapon (
weapon_id INT AUTO_INCREMENT PRIMARY KEY,
damage INT,
fire_rate INT
)""",
"""CREATE TABLE Location (
location_id INT AUTO_INCREMENT PRIMARY KEY,
weapons_available INT,
material_available INT,
distance_from_center DECIMAL(10, 2)
)""",
"""CREATE TABLE Updates (
update_id INT AUTO_INCREMENT PRIMARY KEY,
newly_added_locations TEXT,
newly_added_weapons TEXT,
newly_added_cosmetics TEXT,
shop_schedule TEXT,
locations_balanced TEXT,
weapons_balanced TEXT,
update_date DATE
)""",
"""CREATE TABLE Play (
play_id INT AUTO_INCREMENT PRIMARY KEY,
player_id INT,
weapon_id INT,
location_id INT,
enemies_killed INT,
time_played TIME,
FOREIGN KEY (player_id) REFERENCES Player(id),
FOREIGN KEY (weapon_id) REFERENCES Weapon(weapon_id),
FOREIGN KEY (location_id) REFERENCES Location(location_id)
)""",
"""CREATE TABLE `Match` (
match_id INT AUTO_INCREMENT PRIMARY KEY,
play_id INT,
winner_player_id INT,
date_played DATE,
FOREIGN KEY (play_id) REFERENCES Play(play_id),
FOREIGN KEY (winner_player_id) REFERENCES Player(id)
)""",

"""CREATE TABLE Purchase (
player_id INT,
cosmetic_id INT,
PRIMARY KEY (player_id, cosmetic_id),
FOREIGN KEY (player_id) REFERENCES Player(id),
FOREIGN KEY (cosmetic_id) REFERENCES Cosmetics(cosmetic_id)
)""",
"""CREATE TABLE Friends (
player_id_1 INT,
player_id_2 INT,
PRIMARY KEY (player_id_1, player_id_2),
FOREIGN KEY (player_id_1) REFERENCES Player(id),
FOREIGN KEY (player_id_2) REFERENCES Player(id)
)"""
]
insert_data_queries = [
# Insert data into Cosmetics table
"INSERT INTO Cosmetics (cosmetic_name, cosmetic_type, price) VALUES ('Raven Outfit', 'Outfit', 2000.00)",
"INSERT INTO Cosmetics (cosmetic_name, cosmetic_type, price) VALUES ('Iron Cage', 'Back Bling', 1500.00)",
"INSERT INTO Cosmetics (cosmetic_name, cosmetic_type, price) VALUES ('Bitemark', 'Pickaxe', 1200.00)",
# Insert data into Player table
"INSERT INTO Player (password, currently_equipped) VALUES ('password123', 1)",
"INSERT INTO Player (password, currently_equipped) VALUES ('password234', 2)",
"INSERT INTO Player (password, currently_equipped) VALUES ('password345', 3)"
# Insert data into Weapon table
"INSERT INTO Weapon (damage, fire_rate) VALUES (95, 0.80)",
"INSERT INTO Weapon (damage, fire_rate) VALUES (75, 1.75)",
"INSERT INTO Weapon (damage, fire_rate) VALUES (33, 9.0)",
# Insert data into Location table
"INSERT INTO Location (weapons_available, material_available,distance_from_center) VALUES (5, 500, 0.5)",
"INSERT INTO Location (weapons_available, material_available, distance_from_center) VALUES (10, 1000, 1.0)",
"INSERT INTO Location (weapons_available, material_available, distance_from_center) VALUES (3, 300, 1.5)",
# Insert data into Updates table
"INSERT INTO Updates (newly_added_locations, newly_added_weapons, newly_added_cosmetics, shop_schedule, locations_balanced, weapons_balanced,update_date) VALUES ('Tilted Towers, Haunted Hills', 'Rocket Launcher', 'Ninja Outfit', 'Daily', 'Yes', 'No', '2021-01-01')",
"INSERT INTO Updates (newly_added_locations, newly_added_weapons, newly_added_cosmetics, shop_schedule, locations_balanced, weapons_balanced, update_date) VALUES ('Dusty Depot, Pleasant Park', 'Golden Axe', 'Reaper', 'Weekly', 'No', 'Yes', '2021-01-15')",
"INSERT INTO Updates (newly_added_locations, newly_added_weapons, newly_added_cosmetics, shop_schedule, locations_balanced, weapons_balanced, update_date) VALUES ('Haunted Hills, Dusty Depot', 'Pump Shotgun', 'Iron Cage', 'Monthly', 'Yes', 'Yes', '2021-02-01')",
# Insert data into Play table
"INSERT INTO Play (player_id, weapon_id, location_id, enemies_killed, time_played) VALUES (1, 1, 1, 5, 10)",
"INSERT INTO Play (player_id, weapon_id, location_id, enemies_killed, time_played) VALUES (2, 2, 2, 3, 5)",
"INSERT INTO Play (player_id, weapon_id, location_id, enemies_killed, time_played) VALUES (3, 3, 3, 7, 15)",
# Insert data into Match table
"INSERT INTO `Match` (play_id, winner_player_id, date_played) VALUES (1, 1, '2021-01-01')",
"INSERT INTO `Match` (play_id, winner_player_id, date_played) VALUES (2, 2, '2021-01-15')",
"INSERT INTO `Match` (play_id, winner_player_id, date_played) VALUES (3, 3, '2021-02-01')",
# Insert data into Purchase table
"INSERT INTO Purchase (player_id, cosmetic_id) VALUES (1, 1)",
"INSERT INTO Purchase (player_id, cosmetic_id) VALUES (2, 2)",
"INSERT INTO Purchase (player_id, cosmetic_id) VALUES (3, 3)",
# Insert data into Friends table
"INSERT INTO Friends (player_id_1, player_id_2) VALUES (1, 2)",
"INSERT INTO Friends (player_id_1, player_id_2) VALUES (1, 3)"
"INSERT INTO Friends (player_id_1, player_id_2) VALUES (2, 3)"
]

# Execute queries
for query in queries:
    try:
        cursor.execute(query)
        print(f"Executed: {query}")
    except mysql.connector.Error as err:
        print(f"Error: {err.msg}")

cursor.close()
mydb.close()