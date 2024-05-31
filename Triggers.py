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

# Define SQL statements
create_trigger_sql = """
CREATE TRIGGER adjust_values_on_update
AFTER INSERT ON `Update`
FOR EACH ROW
BEGIN
    DECLARE last_version INT;
    -- Get the ID of the last version
    SELECT MAX(VersionID) INTO last_version FROM `Update`;
    
    -- Adjust values for weapons based on the last version
    UPDATE Weapon
    SET Damage = 0.8 * Damage,
        FireRate = 1.2 * FireRate,
        VersionID = NEW.VersionID
    WHERE VersionID = last_version - 1;
    
    -- Adjust values for locations based on the last version
    UPDATE Location
    SET WeaponsAvailableAmount = WeaponsAvailableAmount * 0.9,
        MaterialAvailableAmount = MaterialAvailableAmount * 1.1,
        VersionID = NEW.VersionID
    WHERE VersionID = last_version - 1;
    
    -- Insert into update audit table
    INSERT INTO UpdateAudit (PreviousVersion, NewVersion, AdjustedValuesDate)
    VALUES (last_version - 1, last_version, NEW.UpdateDate);
END;


CREATE TRIGGER player_delete_trigger
AFTER DELETE ON Player
FOR EACH ROW
BEGIN
    INSERT INTO PlayerAudit (PlayerID, Email, DeletedDate)
    VALUES (OLD.PlayerID, OLD.Email, NOW());
END
"""

# Execute trigger creation SQL
try:
    cursor.execute(create_trigger_sql)
    print("Trigger created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err.msg}")

# Commit changes
mydb.commit()

# Close cursor and connection
cursor.close()
mydb.close()
