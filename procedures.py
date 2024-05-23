import mysql.connector
# Connect to MySQL
mydb = mysql.connector.connect(
user='root',
password='root',
host='localhost',
database='fortnite'
)
# Create cursor
cursor = mydb.cursor()

# Create procedures for CRUD operations on Player table
player_procedures = """
-- Create Procedure for Creating a Player
CREATE PROCEDURE create_player(
IN p_password VARCHAR(255),
IN p_currently_equipped INT
)
BEGIN
INSERT INTO Player (password, currently_equipped)
VALUES (p_password, p_currently_equipped);
END;
-- Create Procedure for Reading Players
CREATE PROCEDURE get_players()
BEGIN
SELECT * FROM Player;
END;
-- Create Procedure for Updating a Player
CREATE PROCEDURE update_player(
IN p_id INT,
IN p_password VARCHAR(255),
IN p_currently_equipped INT
)
BEGIN
UPDATE Player
SET password = p_password, currently_equipped = p_currently_equipped
WHERE id = p_id;
END;
-- Create Procedure for Deleting a Player
CREATE PROCEDURE delete_player(IN p_id INT)
BEGIN
DELETE FROM Player WHERE id = p_id;
END;

"""

cosmetics_procedures = """
-- Create Procedure for Creating a Cosmetic
CREATE PROCEDURE create_cosmetic(
IN p_cosmetic_name VARCHAR(255),
IN p_cosmetic_type VARCHAR(255),
IN p_price DECIMAL(10, 2)
)
BEGIN
INSERT INTO Cosmetics (cosmetic_name, cosmetic_type, price)
VALUES (p_cosmetic_name, p_cosmetic_type, p_price);
END;
-- Create Procedure for Reading Cosmetics
CREATE PROCEDURE get_cosmetics()
BEGIN
SELECT * FROM Cosmetics;
END;
-- Create Procedure for Updating a Cosmetic
CREATE PROCEDURE update_cosmetic(
IN p_cosmetic_id INT,
IN p_cosmetic_name VARCHAR(255),
IN p_cosmetic_type VARCHAR(255),
IN p_price DECIMAL(10, 2)
)
BEGIN
UPDATE Cosmetics
SET cosmetic_name = p_cosmetic_name, cosmetic_type = p_cosmetic_type,
price = p_price
WHERE cosmetic_id = p_cosmetic_id;
END;
-- Create Procedure for Deleting a Cosmetic
CREATE PROCEDURE delete_cosmetic(IN p_cosmetic_id INT)
BEGIN
DELETE FROM Cosmetics WHERE cosmetic_id = p_cosmetic_id;
END;
"""
# Add procedures for other tables similarly
weapon_procedures = """
-- Create Procedure for Creating a Weapon

CREATE PROCEDURE create_weapon(
IN p_damage INT,
IN p_fire_rate INT
)
BEGIN
INSERT INTO Weapon (damage, fire_rate)
VALUES (p_damage, p_fire_rate);
END;
-- Create Procedure for Reading Weapons
CREATE PROCEDURE get_weapons()
BEGIN
SELECT * FROM Weapon;
END;
-- Create Procedure for Updating a Weapon
CREATE PROCEDURE update_weapon(
IN p_weapon_id INT,
IN p_damage INT,
IN p_fire_rate INT
)
BEGIN
UPDATE Weapon
SET damage = p_damage, fire_rate = p_fire_rate
WHERE weapon_id = p_weapon_id;
END;

-- Create Procedure for Deleting a Weapon
CREATE PROCEDURE delete_weapon(IN p_weapon_id INT)
BEGIN
DELETE FROM Weapon WHERE weapon_id = p_weapon_id;
END;
"""

# Add procedures for other tables similarly
location_procedures = """
-- Create Procedure for Creating a Location
CREATE PROCEDURE create_location(
IN p_weapons_available INT,
IN p_material_available INT,
IN p_distance_from_center DECIMAL(10, 2)
)

BEGIN
INSERT INTO Location (weapons_available, material_available,
distance_from_center)
VALUES (p_weapons_available, p_material_available,
p_distance_from_center);
END;
-- Create Procedure for Reading Locations
CREATE PROCEDURE get_locations()
BEGIN
SELECT * FROM Location;
END;
-- Create Procedure for Updating a Location
CREATE PROCEDURE update_location(
IN p_location_id INT,
IN p_weapons_available INT,
IN p_material_available INT,
IN p_distance_from_center DECIMAL(10, 2)
)
BEGIN
UPDATE Location
SET weapons_available = p_weapons_available, material_available =
p_material_available, distance_from_center = p_distance_from_center
WHERE location_id = p_location_id;
END;

-- Create Procedure for Deleting a Location
CREATE PROCEDURE delete_location(IN p_location_id INT)
BEGIN
DELETE FROM Location WHERE location_id = p_location_id;
END;

"""
# Add procedures for other tables similarly
updates_procedures = """
-- Create Procedure for Creating an Update
CREATE PROCEDURE create_update(
IN p_newly_added_locations TEXT,
IN p_newly_added_weapons TEXT,
IN p_newly_added_cosmetics TEXT,
IN p_shop_schedule TEXT,

IN p_locations_balanced TEXT,
IN p_weapons_balanced TEXT,
IN p_update_date DATE
)
BEGIN
INSERT INTO Updates (newly_added_locations, newly_added_weapons,
newly_added_cosmetics, shop_schedule, locations_balanced, weapons_balanced,
update_date)
VALUES (p_newly_added_locations, p_newly_added_weapons,
p_newly_added_cosmetics, p_shop_schedule, p_locations_balanced,
p_weapons_balanced, p_update_date);
END;
-- Create Procedure for Reading Updates
CREATE PROCEDURE get_updates()
BEGIN
SELECT * FROM Updates;
END;
-- Create Procedure for Updating an Update
CREATE PROCEDURE update_update(
IN p_update_id INT,
IN p_newly_added_locations TEXT,
IN p_newly_added_weapons TEXT,
IN p_newly_added_cosmetics TEXT,
IN p_shop_schedule TEXT,
IN p_locations_balanced TEXT,
IN p_weapons_balanced TEXT,
IN p_update_date DATE
)
BEGIN
UPDATE Updates
SET newly_added_locations = p_newly_added_locations, newly_added_weapons =
p_newly_added_weapons, newly_added_cosmetics = p_newly_added_cosmetics,
shop_schedule = p_shop_schedule, locations_balanced = p_locations_balanced,
weapons_balanced = p_weapons_balanced, update_date = p_update_date
WHERE update_id = p_update_id;
END;

-- Create Procedure for Deleting an Update
CREATE PROCEDURE delete_update(IN p_update_id INT)
BEGIN
DELETE FROM Updates WHERE update_id = p_update_id;
END;

"""
# Add procedures for other tables similarly
play_procedures = """
-- Create Procedure for Creating a Play
CREATE PROCEDURE create_play(
IN p_player_id INT,
IN p_weapon_id INT,
IN p_location_id INT,
IN p_enemies_killed INT,
IN p_time_played TIME
)
BEGIN
INSERT INTO Play (player_id, weapon_id, location_id, enemies_killed,
time_played)
VALUES (p_player_id, p_weapon_id, p_location_id, p_enemies_killed,
p_time_played);
END;
-- Create Procedure for Reading Plays
CREATE PROCEDURE get_plays()
BEGIN
SELECT * FROM Play;
END;
-- Create Procedure for Updating a Play
CREATE PROCEDURE update_play(
IN p_play_id INT,
IN p_player_id INT,
IN p_weapon_id INT,
IN p_location_id INT,
IN p_enemies_killed INT,
IN p_time_played TIME
)
BEGIN
UPDATE Play
SET player_id = p_player_id, weapon_id = p_weapon_id, location_id =
p_location_id, enemies_killed = p_enemies_killed, time_played = p_time_played
WHERE play_id = p_play_id;
END;
-- Create Procedure for Deleting a Play
CREATE PROCEDURE delete_play(IN p_play_id INT)

BEGIN
DELETE FROM Play WHERE play_id = p_play_id;
END;
"""
# Add procedures for other tables similarly
match_procedures = """
-- Create Procedure for Creating a Match
CREATE PROCEDURE create_match(
IN p_play_id INT,
IN p_winner_player_id INT,
IN p_date_played DATE
)
BEGIN
INSERT INTO `Match` (play_id, winner_player_id, date_played)
VALUES (p_play_id, p_winner_player_id, p_date_played);
END;
-- Create Procedure for Reading Matches
CREATE PROCEDURE get_matches()
BEGIN
SELECT * FROM `Match`;
END;
-- Create Procedure for Updating a Match
CREATE PROCEDURE update_match(
IN p_match_id INT,
IN p_play_id INT,
IN p_winner_player_id INT,
IN p_date_played DATE
)
BEGIN
UPDATE `Match`
SET play_id = p_play_id, winner_player_id = p_winner_player_id,
date_played = p_date_played
WHERE match_id = p_match_id;
END;
-- Create Procedure for Deleting a Match
CREATE PROCEDURE delete_match(IN p_match_id INT)
BEGIN
DELETE FROM `Match` WHERE match_id = p_match_id;
END;
"""

# Add procedures for other tables similarly

purchase_procedures = """
-- Create Procedure for Creating a Purchase
CREATE PROCEDURE create_purchase(
IN p_player_id INT,
IN p_cosmetic_id INT
)

BEGIN
INSERT INTO Purchase (player_id, cosmetic_id)
VALUES (p_player_id, p_cosmetic_id);
END;
-- Create Procedure for Reading Purchases
CREATE PROCEDURE get_purchases()
BEGIN
SELECT * FROM Purchase;
END;
-- Create Procedure for Deleting a Purchase
CREATE PROCEDURE delete_purchase(IN p_player_id INT, IN p_cosmetic_id INT)
BEGIN
DELETE FROM Purchase WHERE player_id = p_player_id AND cosmetic_id =
p_cosmetic_id;
END;
"""
# Add procedures for other tables similarly
friends_procedures = """
-- Create Procedure for Creating a Friend
CREATE PROCEDURE create_friend(
IN p_player_id_1 INT,
IN p_player_id_2 INT
)
BEGIN
INSERT INTO Friends (player_id_1, player_id_2)
VALUES (p_player_id_1, p_player_id_2);
END;

-- Create Procedure for Reading Friends
CREATE PROCEDURE get_friends()
BEGIN

SELECT * FROM Friends;
END;
-- Create Procedure for Deleting a Friend
CREATE PROCEDURE delete_friend(IN p_player_id_1 INT, IN p_player_id_2 INT)
BEGIN
DELETE FROM Friends WHERE player_id_1 = p_player_id_1 AND player_id_2 =
p_player_id_2;
END;
"""

# Create procedures for CRUD operations on Player table
procedures = [
player_procedures,
cosmetics_procedures,
weapon_procedures,
location_procedures,
updates_procedures,
play_procedures,
match_procedures,
purchase_procedures,
friends_procedures
]
# Execute procedures
for procedure in procedures:
    try:
        cursor.execute(procedure)
        print(f"Executed: {procedure}")
    except mysql.connector.Error as err:
        print(f"Error: {err.msg}")

# Commit changes
mydb.commit()

# Close connection
cursor.close()
mydb.close()

