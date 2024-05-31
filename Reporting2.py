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

# List of stored procedures to execute
queries = [
    """
   CREATE PROCEDURE location_stats_by_update()
BEGIN
    SELECT 
        l.LocationName,
        u.UpdateDate,
        COUNT(m.MatchID) AS total_matches,
        SUM(CASE WHEN m.WinnerPlayerID = p.PlayerID THEN 1 ELSE 0 END) AS wins,
        (SUM(CASE WHEN m.WinnerPlayerID = p.PlayerID THEN 1 ELSE 0 END) / COUNT(m.MatchID)) * 100 AS win_rate,
        SUM(p.Kills) AS total_kills
    FROM 
        `Match` m
    JOIN 
        Play p ON m.MatchID = p.MatchID
    JOIN 
        Location l ON p.LocationVisited = l.LocationID
    JOIN 
        `Update` u ON l.VersionID = u.VersionID
    WHERE
        m.DatePlayed >= u.UpdateDate
    GROUP BY 
        l.LocationID, u.UpdateDate
    ORDER BY 
        u.UpdateDate DESC, win_rate DESC;
END;

    """,
    """
   CREATE PROCEDURE weapon_stats_by_update()
BEGIN
    SELECT 
        w.WeaponName,
        u.UpdateDate,
        COUNT(m.MatchID) AS total_matches,
        SUM(CASE WHEN m.WinnerPlayerID = p.PlayerID THEN 1 ELSE 0 END) AS wins,
        (SUM(CASE WHEN m.WinnerPlayerID = p.PlayerID THEN 1 ELSE 0 END) / COUNT(m.MatchID)) * 100 AS win_rate,
        SUM(p.Kills) AS total_kills
    FROM 
        `Match` m
    JOIN 
        Play p ON m.MatchID = p.MatchID
    JOIN 
        Weapon w ON p.WeaponUsed = w.WeaponID
    JOIN 
        `Update` u ON w.VersionID = u.VersionID
    WHERE
        m.DatePlayed >= u.UpdateDate
    GROUP BY 
        w.WeaponID, u.UpdateDate
    ORDER BY 
        u.UpdateDate DESC, win_rate DESC;
END;

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
