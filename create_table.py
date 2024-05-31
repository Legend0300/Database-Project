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


queries = ["""
CREATE TABLE `Update` (
    VersionID INT AUTO_INCREMENT PRIMARY KEY,
    UpdateDate DATE
);
           

CREATE TABLE Cosmetic (
    CosmeticID INT AUTO_INCREMENT PRIMARY KEY,
    CosmeticName VARCHAR(255),
    Price DECIMAL(10, 2),
    VersionID INT,
    FOREIGN KEY (VersionID) REFERENCES `Update`(VersionID)
);           
           
CREATE TABLE Player (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY,
    Email VARCHAR(255) UNIQUE,
    Password VARCHAR(255),
    CosmeticEquipped INT,
    FOREIGN KEY (CosmeticEquipped) REFERENCES Cosmetic(CosmeticID) NULL
);

CREATE TABLE Purchase (
    PlayerID INT,
    CosmeticID INT,
    DatePurchased DATE,
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
    FOREIGN KEY (CosmeticID) REFERENCES Cosmetic(CosmeticID),
    PRIMARY KEY (PlayerID, CosmeticID)
);

CREATE TABLE Friendship (
    PlayerID1 INT,
    PlayerID2 INT,
    FOREIGN KEY (PlayerID1) REFERENCES Player(PlayerID),
    FOREIGN KEY (PlayerID2) REFERENCES Player(PlayerID),
    PRIMARY KEY (PlayerID1, PlayerID2)
);

CREATE TABLE Weapon (
    WeaponID INT AUTO_INCREMENT PRIMARY KEY,
    WeaponName VARCHAR(255),
    Damage INT,
    FireRate DECIMAL(5, 2),
    VersionID INT,
    FOREIGN KEY (VersionID) REFERENCES `Update`(VersionID)
);

CREATE TABLE Location (
    LocationID INT AUTO_INCREMENT PRIMARY KEY,
    LocationName VARCHAR(255),
    WeaponsAvailableAmount INT,
    MaterialAvailableAmount INT,
    DistanceFromCenter DECIMAL(10, 2),
    VersionID INT,
    FOREIGN KEY (VersionID) REFERENCES `Update`(VersionID)
);

CREATE TABLE `Match` (
    MatchID INT AUTO_INCREMENT PRIMARY KEY,
    DatePlayed DATE,
    WinnerPlayerID INT,
    FOREIGN KEY (WinnerPlayerID) REFERENCES Player(PlayerID)
);

CREATE TABLE Play (
    PlayerID INT,
    MatchID INT,
    Kills INT default 0,
    TimePlayed TIME,
    WeaponUsed INT,
    LocationVisited INT,
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
    FOREIGN KEY (MatchID) REFERENCES `Match`(MatchID),
    FOREIGN KEY (WeaponUsed) REFERENCES Weapon(WeaponID),
    FOREIGN KEY (LocationVisited) REFERENCES Location(LocationID),
    PRIMARY KEY (PlayerID, MatchID)
);


"""]


# Define the insertion queries in the correct order
insertion_queries = [
    # Populate Update table
    """
    INSERT INTO `Update` (VersionID, UpdateDate) VALUES
    (1, '2024-05-01');
    """,
    # Populate Cosmetic table
    """
    INSERT INTO Cosmetic (CosmeticID, CosmeticName, Price, VersionID) VALUES
    (1, 'Fortnite Skin 1', 10.99, 1),
    (2, 'Fortnite Skin 2', 8.99, 1),
    (3, 'Fortnite Skin 3', 12.99, 1);
    """,
    # Populate Player table
    """
    INSERT INTO Player (PlayerID, Email, Password, CosmeticEquipped) VALUES
    (1, 'player1@example.com', 'password1', 1),
    (2, 'player2@example.com', 'password2', 2),
    (3, 'player3@example.com', 'password3', 3),
    (4, 'player4@example.com', 'password4', NULL);
    """,
    # Populate Weapon table
    """
    INSERT INTO Weapon (WeaponID, WeaponName, Damage, FireRate, VersionID) VALUES
    (1, 'Shotgun', 50, 0.5, 1),
    (2, 'Assault Rifle', 30, 0.1, 1),
    (3, 'Sniper Rifle', 100, 1, 1);
    """,
    # Populate Location table
    """
    INSERT INTO Location (LocationID, LocationName, WeaponsAvailableAmount, MaterialAvailableAmount, DistanceFromCenter, VersionID) VALUES
    (1, 'Tilted Towers', 10, 100, 20.5, 1),
    (2, 'Pleasant Park', 8, 90, 15.2, 1),
    (3, 'Retail Row', 6, 80, 18.7, 1);
    """,
    # Populate Match table
    """
    INSERT INTO `Match` (MatchID, DatePlayed, WinnerPlayerID) VALUES
    (1, '2024-05-20', 1),
    (2, '2024-05-21', 2),
    (3, '2024-05-22', 3),
    (4, '2024-05-23', 1);
    """,
    # Populate Purchase table
    """
    INSERT INTO Purchase (PlayerID, CosmeticID, DatePurchased) VALUES
    (1, 1, '2024-05-20'),
    (2, 2, '2024-05-21'),
    (3, 3, '2024-05-22'),
    (1, 3, '2024-05-23');
    """,
    # Populate Friendship table
    """
    INSERT INTO Friendship (PlayerID1, PlayerID2) VALUES
    (1, 2),
    (1, 3),
    (2, 3);
    """,
    # Populate Play table
    """
    INSERT INTO Play (PlayerID, MatchID, Kills, TimePlayed, WeaponUsed, LocationVisited) VALUES
    (1, 1, 10, '00:15:00', 1, 1),
    (2, 2, 8, '00:12:30', 2, 2),
    (3, 3, 12, '00:18:45', 3, 3),
    (1, 4, 15, '00:20:00', 1, 1);
    """
]

# Execute insertion queries
for query in insertion_queries:
    try:
        cursor.execute(query)
        print(f"Executed: {query.split()[2]}")  # Print operation executed
    except mysql.connector.Error as err:
        print(f"Error: {err.msg}")

# Commit changes
mydb.commit()

# Close cursor and connection
cursor.close()
mydb.close()
