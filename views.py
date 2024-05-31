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

materialized_views_sql = [
    """
    CREATE VIEW player_stats AS
    SELECT
        p.PlayerID,
        p.Email,
        COUNT(pl.LocationVisited) AS LocationsVisited,
        SUM(pl.Kills) AS TotalKills,
        SUM(pl.Kills) / COUNT(pl.LocationVisited) AS KD_Ratio,
        (
            SELECT w.WeaponName
            FROM Weapon w
            JOIN Play pl ON pl.WeaponUsed = w.WeaponID
            WHERE pl.PlayerID = p.PlayerID
            GROUP BY pl.WeaponUsed
            ORDER BY SUM(pl.Kills) DESC
            LIMIT 1
        ) AS BestWeapon,
        (
            SELECT COUNT(m.MatchID)
            FROM `Match` m
            JOIN Play pl ON pl.MatchID = m.MatchID
            WHERE m.WinnerPlayerID = p.PlayerID
        ) / COUNT(pl.MatchID) AS WinRate
    FROM Player p
    JOIN Play pl ON pl.PlayerID = p.PlayerID
    GROUP BY p.PlayerID, p.Email
    """
    # Define more regular views here if needed
]




# Define SQL statements for complex views
complex_views_sql = [
    # Highest Kills (Top 10)
    """
    CREATE VIEW highest_kills AS
    SELECT
        p.PlayerID,
        p.Email,
        SUM(pl.Kills) AS TotalKills
    FROM Player p
    JOIN Play pl ON pl.PlayerID = p.PlayerID
    GROUP BY p.PlayerID, p.Email
    ORDER BY TotalKills DESC
    LIMIT 10;
    """,
    # Highest Wins (Top 10)
    """
    CREATE VIEW highest_wins AS
    SELECT
        p.PlayerID,
        p.Email,
        COUNT(m.MatchID) AS TotalWins
    FROM Player p
    JOIN `Match` m ON m.WinnerPlayerID = p.PlayerID
    GROUP BY p.PlayerID, p.Email
    ORDER BY TotalWins DESC
    LIMIT 10;
    """,
    # Highest KD Ratio (Top 10)
    """
    CREATE VIEW highest_kd_ratio AS
    SELECT
        p.PlayerID,
        p.Email,
        SUM(pl.Kills) / COUNT(pl.LocationVisited) AS KD_Ratio
    FROM Player p
    JOIN Play pl ON pl.PlayerID = p.PlayerID
    GROUP BY p.PlayerID, p.Email
    ORDER BY KD_Ratio DESC
    LIMIT 10;
    """,
    # Highest Win Rate (Top 10)
    """
    CREATE VIEW highest_winrate AS
    SELECT
        p.PlayerID,
        p.Email,
        (
            SELECT COUNT(m.MatchID)
            FROM `Match` m
            JOIN Play pl ON pl.MatchID = m.MatchID
            WHERE m.WinnerPlayerID = p.PlayerID
        ) / COUNT(m.MatchID) AS WinRate
    FROM Player p
    JOIN `Match` m ON m.WinnerPlayerID = p.PlayerID
    GROUP BY p.PlayerID, p.Email
    ORDER BY WinRate DESC
    LIMIT 10;
    """
    # Define more complex views here if needed
]

# Execute materialized views creation SQL
for sql in materialized_views_sql:
    try:
        cursor.execute(sql)
        print("Materialized view created successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err.msg}")

# # Execute complex views creation SQL
# for sql in complex_views_sql:
#     try:
#         cursor.execute(sql)
#         print("Complex view created successfully.")
#     except mysql.connector.Error as err:
#         print(f"Error: {err.msg}")

# Commit changes
mydb.commit()

# Close cursor and connection
cursor.close()
mydb.close()
