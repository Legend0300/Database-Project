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

# List of queries to execute
queries = [
    """
    CREATE PROCEDURE winrate_for_locations()
    BEGIN
        SELECT 
            l.LocationName,
            COUNT(m.MatchID) AS total_matches,
            SUM(CASE WHEN m.WinnerPlayerID = p.PlayerID THEN 1 ELSE 0 END) AS wins,
            (SUM(CASE WHEN m.WinnerPlayerID = p.PlayerID THEN 1 ELSE 0 END) / COUNT(m.MatchID)) * 100 AS win_rate
        FROM 
            `Match` m
        JOIN 
            Play p ON m.MatchID = p.MatchID
        JOIN 
            Location l ON p.LocationVisited = l.LocationID
        GROUP BY 
            l.LocationID
        ORDER BY 
            win_rate DESC;
    END
    """,
    """
    CREATE PROCEDURE winrate_for_weapons()
    BEGIN
        SELECT 
            w.WeaponName,
            COUNT(m.MatchID) AS total_matches,
            SUM(CASE WHEN m.WinnerPlayerID = p.PlayerID THEN 1 ELSE 0 END) AS wins,
            (SUM(CASE WHEN m.WinnerPlayerID = p.PlayerID THEN 1 ELSE 0 END) / COUNT(m.MatchID)) * 100 AS win_rate
        FROM 
            `Match` m
        JOIN 
            Play p ON m.MatchID = p.MatchID
        JOIN 
            Weapon w ON p.WeaponUsed = w.WeaponID
        GROUP BY 
            w.WeaponID
        ORDER BY 
            win_rate DESC;
    END
    """,
    """
    CREATE PROCEDURE kills_for_locations()
    BEGIN
        SELECT 
            l.LocationName,
            SUM(p.Kills) AS total_kills
        FROM 
            Play p
        JOIN 
            Location l ON p.LocationVisited = l.LocationID
        GROUP BY 
            l.LocationID
        ORDER BY 
            total_kills DESC;
    END
    """,
    """
    CREATE PROCEDURE kills_for_weapons()
    BEGIN
        SELECT 
            w.WeaponName,
            SUM(p.Kills) AS total_kills
        FROM 
            Play p
        JOIN 
            Weapon w ON p.WeaponUsed = w.WeaponID
        GROUP BY 
            w.WeaponID
        ORDER BY 
            total_kills DESC;
    END
    """,
    """
    CREATE PROCEDURE player_stats()
    BEGIN
        SELECT 
            p.PlayerID,
            p.Email,
            COUNT(pl.MatchID) AS total_matches,
            SUM(pl.Kills) AS total_kills,
            SEC_TO_TIME(SUM(TIME_TO_SEC(pl.TimePlayed))) AS total_time_played
        FROM 
            Player p
        JOIN 
            Play pl ON p.PlayerID = pl.PlayerID
        GROUP BY 
            p.PlayerID
        ORDER BY 
            total_kills DESC;
    END
    """
]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        print("Procedure executed successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err.msg}")

# Commit changes
mydb.commit()

# Close cursor and connection
cursor.close()
mydb.close()
