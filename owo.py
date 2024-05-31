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

# Create tables
create_tables = """


-- Create Update table
CREATE TABLE `Update` (
    VersionID INT AUTO_INCREMENT PRIMARY KEY,
    UpdateDate DATE
);


-- Create Cosmetic table
CREATE TABLE Cosmetic (
    CosmeticID INT AUTO_INCREMENT PRIMARY KEY,
    CosmeticName VARCHAR(255),
    Price DECIMAL(10, 2),
    VersionID INT,
    CONSTRAINT fk_version_cosmetic FOREIGN KEY (VersionID) REFERENCES `Update`(VersionID)
);


-- Create Player table
CREATE TABLE Player (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY,
    Email VARCHAR(255) UNIQUE,
    Password VARCHAR(255),
    CosmeticEquipped INT,
    CONSTRAINT fk_cosmetic FOREIGN KEY (CosmeticEquipped) REFERENCES Cosmetic(CosmeticID)
);


-- Create Weapon table
CREATE TABLE Weapon (
    WeaponID INT AUTO_INCREMENT PRIMARY KEY,
    WeaponName VARCHAR(255),
    Damage INT,
    FireRate DECIMAL(5, 2),
    VersionID INT,
    CONSTRAINT fk_version_weapon FOREIGN KEY (VersionID) REFERENCES Update(VersionID)
);

-- Create Location table
CREATE TABLE Location (
    LocationID INT AUTO_INCREMENT PRIMARY KEY,
    LocationName VARCHAR(255),
    WeaponsAvailableAmount INT,
    MaterialAvailableAmount INT,
    DistanceFromCenter DECIMAL(10, 2),
    VersionID INT,
    CONSTRAINT fk_version_location FOREIGN KEY (VersionID) REFERENCES Update(VersionID)
);


-- Create Match table
CREATE TABLE `Match` (
    MatchID INT AUTO_INCREMENT PRIMARY KEY,
    DatePlayed DATE,
    WinnerPlayerID INT,
    CONSTRAINT fk_winner_player FOREIGN KEY (WinnerPlayerID) REFERENCES Player(PlayerID)
);

-- Create Play table
CREATE TABLE Play (
    PlayerID INT,
    MatchID INT,
    Kills INT,
    TimePlayed TIME,
    WeaponUsed INT,
    LocationVisited INT,
    CONSTRAINT fk_player_play FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
    CONSTRAINT fk_match_play FOREIGN KEY (MatchID) REFERENCES `Match`(MatchID),
    CONSTRAINT fk_weapon_play FOREIGN KEY (WeaponUsed) REFERENCES Weapon(WeaponID),
    CONSTRAINT fk_location_play FOREIGN KEY (LocationVisited) REFERENCES Location(LocationID),
    PRIMARY KEY (PlayerID, MatchID)
);

-- Create Purchase table
CREATE TABLE Purchase (
    PlayerID INT,
    CosmeticID INT,
    DatePurchased DATE,
    CONSTRAINT fk_player_purchase FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
    CONSTRAINT fk_cosmetic_purchase FOREIGN KEY (CosmeticID) REFERENCES Cosmetic(CosmeticID),
    PRIMARY KEY (PlayerID, CosmeticID)
);

-- Create Friendship table
CREATE TABLE Friendship (
    PlayerID1 INT,
    PlayerID2 INT,
    CONSTRAINT fk_player1_friendship FOREIGN KEY (PlayerID1) REFERENCES Player(PlayerID),
    CONSTRAINT fk_player2_friendship FOREIGN KEY (PlayerID2) REFERENCES Player(PlayerID),
    PRIMARY KEY (PlayerID1, PlayerID2)
);
"""

# Execute table creation queries
try:
    cursor.execute(create_tables, multi=True)
    print("Tables created successfully")
except mysql.connector.Error as err:
    print(f"Error: {err.msg}")

# Create procedures for CRUD operations on Player table
player_procedures = """
-- Create Procedure for Creating a Player
CREATE PROCEDURE create_player(
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255),
    IN p_cosmetic_equipped INT
)
BEGIN
    INSERT INTO Player (Email, Password, CosmeticEquipped)
    VALUES (p_email, p_password, p_cosmetic_equipped);
END;

-- Create Procedure for Reading Players
CREATE PROCEDURE get_players()
BEGIN
    SELECT * FROM Player;
END;

-- Create Procedure for Updating a Player
CREATE PROCEDURE update_player(
    IN p_player_id INT,
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255),
    IN p_cosmetic_equipped INT
)
BEGIN
    UPDATE Player
    SET Email = p_email, Password = p_password, CosmeticEquipped = p_cosmetic_equipped
    WHERE PlayerID = p_player_id;
END;

-- Create Procedure for Deleting a Player
CREATE PROCEDURE delete_player(IN p_player_id INT)
BEGIN
    DELETE FROM Player WHERE PlayerID = p_player_id;
END;
"""

# Add procedures for other tables similarly
cosmetics_procedures = """
-- Create Procedure for Creating a Cosmetic
CREATE PROCEDURE create_cosmetic(
    IN p_cosmetic_name VARCHAR(255),
    IN p_price DECIMAL(10, 2),
    IN p_version_id INT
)
BEGIN
    INSERT INTO Cosmetic (CosmeticName, Price, VersionID)
    VALUES (p_cosmetic_name, p_price, p_version_id);
END;

-- Create Procedure for Reading Cosmetics
CREATE PROCEDURE get_cosmetics()
BEGIN
    SELECT * FROM Cosmetic;
END;

-- Create Procedure for Updating a Cosmetic
CREATE PROCEDURE update_cosmetic(
    IN p_cosmetic_id INT,
    IN p_cosmetic_name VARCHAR(255),
    IN p_price DECIMAL(10, 2),
    IN p_version_id INT
)
BEGIN
    UPDATE Cosmetic
    SET CosmeticName = p_cosmetic_name, Price = p_price, VersionID = p_version_id
    WHERE CosmeticID = p_cosmetic_id;
END;

-- Create Procedure for Deleting a Cosmetic
CREATE PROCEDURE delete_cosmetic(IN p_cosmetic_id INT)
BEGIN
    DELETE FROM Cosmetic WHERE CosmeticID = p_cosmetic_id;
END;
"""

# Add procedures for other tables similarly
weapon_procedures = """
-- Create Procedure for Creating a Weapon
CREATE PROCEDURE create_weapon(
    IN p_weapon_name VARCHAR(255),
    IN p_damage INT,
    IN p_fire_rate DECIMAL(5, 2),
    IN p_version_id INT
)
BEGIN
    INSERT INTO Weapon (WeaponName, Damage, FireRate, VersionID)
    VALUES (p_weapon_name, p_damage, p_fire_rate, p_version_id);
END;

-- Create Procedure for Reading Weapons
CREATE PROCEDURE get_weapons()
BEGIN
    SELECT * FROM Weapon;
END;

-- Create Procedure for Updating a Weapon
CREATE PROCEDURE update_weapon(
    IN p_weapon_id INT,
    IN p_weapon_name VARCHAR(255),
    IN p_damage INT,
    IN p_fire_rate DECIMAL(5, 2),
    IN p_version_id INT
)
BEGIN
    UPDATE Weapon
    SET WeaponName = p_weapon_name, Damage = p_damage, FireRate = p_fire_rate, VersionID = p_version_id
    WHERE WeaponID = p_weapon_id;
END;

-- Create Procedure for Deleting a Weapon
CREATE PROCEDURE delete_weapon(IN p_weapon_id INT)
BEGIN
    DELETE FROM Weapon WHERE WeaponID = p_weapon_id;
END;
"""

# Add procedures for other tables similarly
location_procedures = """
-- Create Procedure for Creating a Location
CREATE PROCEDURE create_location(
    IN p_location_name VARCHAR(255),
    IN p_weapons_available_amount INT,
    IN p_material_available_amount INT,
    IN p_distance_from_center DECIMAL(10, 2),
    IN p_version_id INT
)
BEGIN
    INSERT INTO Location (LocationName, WeaponsAvailableAmount, MaterialAvailableAmount, DistanceFromCenter, VersionID)
    VALUES (p_location_name, p_weapons_available_amount, p_material_available_amount, p_distance_from_center, p_version_id);
END;

-- Create Procedure for Reading Locations
CREATE PROCEDURE get_locations()
BEGIN
    SELECT * FROM Location;
END;

-- Create Procedure for Updating a Location
CREATE PROCEDURE update_location(
    IN p_location_id INT,
    IN p_location_name VARCHAR(255),
    IN p_weapons_available_amount INT,
    IN p_material_available_amount INT,
    IN p_distance_from_center DECIMAL(10, 2),
    IN p_version_id INT
)
BEGIN
    UPDATE Location
    SET LocationName = p_location_name, WeaponsAvailableAmount = p_weapons_available_amount, MaterialAvailableAmount = p_material_available_amount, DistanceFromCenter = p_distance_from_center, VersionID = p_version_id
    WHERE LocationID = p_location_id;
END;

-- Create Procedure for Deleting a Location
CREATE PROCEDURE delete_location(IN p_location_id INT)
BEGIN
    DELETE FROM Location WHERE LocationID = p_location_id;
END;
"""

# Add procedures for other tables similarly
updates_procedures = """
-- Create Procedure for Creating an Update
CREATE PROCEDURE create_update(
    IN p_update_date DATE
)
BEGIN
    INSERT INTO `Update` (UpdateDate)
    VALUES (p_update_date);
END;

-- Create Procedure for Reading Updates
CREATE PROCEDURE get_updates()
BEGIN
    SELECT * FROM `Update`;
END;

-- Create Procedure for Updating an Update
CREATE PROCEDURE update_update(
    IN p_version_id INT,
    IN p_update_date DATE
)
BEGIN
    UPDATE `Update`
    SET UpdateDate = p_update_date
    WHERE VersionID = p_version_id;
END;

-- Create Procedure for Deleting an Update
CREATE PROCEDURE delete_update(IN p_version_id INT)
BEGIN
    DELETE FROM `Update` WHERE VersionID = p_version_id;
END;
"""

# Add procedures for other tables similarly
play_procedures = """
-- Create Procedure for Creating a Play
CREATE PROCEDURE create_play(
    IN p_player_id INT,
    IN p_match_id INT,
    IN p_kills INT,
    IN p_time_played TIME,
    IN p_weapon_used INT,
    IN p_location_visited INT
)
BEGIN
    INSERT INTO Play (PlayerID, MatchID, Kills, TimePlayed, WeaponUsed, LocationVisited)
    VALUES (p_player_id, p_match_id, p_kills, p_time_played, p_weapon_used, p_location_visited);
END;

-- Create Procedure for Reading Plays
CREATE PROCEDURE get_plays()
BEGIN
    SELECT * FROM Play;
END;

-- Create Procedure for Updating a Play
CREATE PROCEDURE update_play(
    IN p_player_id INT,
    IN p_match_id INT,
    IN p_kills INT,
    IN p_time_played TIME,
    IN p_weapon_used INT,
    IN p_location_visited INT
)
BEGIN
    UPDATE Play
    SET Kills = p_kills, TimePlayed = p_time_played, WeaponUsed = p_weapon_used, LocationVisited = p_location_visited
    WHERE PlayerID = p_player_id AND MatchID = p_match_id;
END;

-- Create Procedure for Deleting a Play
CREATE PROCEDURE delete_play(
    IN p_player_id INT,
    IN p_match_id INT
)
BEGIN
    DELETE FROM Play WHERE PlayerID = p_player_id AND MatchID = p_match_id;
END;
"""

# Add procedures for other tables similarly
match_procedures = """
-- Create Procedure for Creating a Match
CREATE PROCEDURE create_match(
    IN p_date_played DATE,
    IN p_winner_player_id INT
)
BEGIN
    INSERT INTO `Match` (DatePlayed, WinnerPlayerID)
    VALUES (p_date_played, p_winner_player_id);
END;

-- Create Procedure for Reading Matches
CREATE PROCEDURE get_matches()
BEGIN
    SELECT * FROM `Match`;
END;

-- Create Procedure for Updating a Match
CREATE PROCEDURE update_match(
    IN p_match_id INT,
    IN p_date_played DATE,
    IN p_winner_player_id INT
)
BEGIN
    UPDATE `Match`
    SET DatePlayed = p_date_played, WinnerPlayerID = p_winner_player_id
    WHERE MatchID = p_match_id;
END;

-- Create Procedure for Deleting a Match
CREATE PROCEDURE delete_match(IN p_match_id INT)
BEGIN
    DELETE FROM `Match` WHERE MatchID = p_match_id;
END;
"""

# Add procedures for other tables similarly
purchase_procedures = """
-- Create Procedure for Creating a Purchase
CREATE PROCEDURE create_purchase(
    IN p_player_id INT,
    IN p_cosmetic_id INT,
    IN p_date_purchased DATE
)
BEGIN
    INSERT INTO Purchase (PlayerID, CosmeticID, DatePurchased)
    VALUES (p_player_id, p_cosmetic_id, p_date_purchased);
END;

-- Create Procedure for Reading Purchases
CREATE PROCEDURE get_purchases()
BEGIN
    SELECT * FROM Purchase;
END;

-- Create Procedure for Deleting a Purchase
CREATE PROCEDURE delete_purchase(
    IN p_player_id INT,
    IN p_cosmetic_id INT
)
BEGIN
    DELETE FROM Purchase WHERE PlayerID = p_player_id AND CosmeticID = p_cosmetic_id;
END;
"""

# Add procedures for other tables similarly
friends_procedures = """
-- Create Procedure for Creating a Friendship
CREATE PROCEDURE create_friendship(
    IN p_player_id_1 INT,
    IN p_player_id_2 INT
)
BEGIN
    INSERT INTO Friendship (PlayerID1, PlayerID2)
    VALUES (p_player_id_1, p_player_id_2);
END;

-- Create Procedure for Reading Friendships
CREATE PROCEDURE get_friendships()
BEGIN
    SELECT * FROM Friendship;
END;

-- Create Procedure for Deleting a Friendship
CREATE PROCEDURE delete_friendship(
    IN p_player_id_1 INT,
    IN p_player_id_2 INT
)
BEGIN
    DELETE FROM Friendship WHERE PlayerID1 = p_player_id_1 AND PlayerID2 = p_player_id_2;
END;
"""

# Execute procedures
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

# Commit changes
mydb.commit()

# Close connection
cursor.close()
mydb.close()
