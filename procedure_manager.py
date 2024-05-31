import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor(buffered=True)

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def execute_procedure(self, procedure_name, *args):
        try:
            self.cursor.callproc(procedure_name, args)
            result_sets = [result.fetchall() for result in self.cursor.stored_results()]
            self.connection.commit()
            return result_sets
        except mysql.connector.Error as err:
            print(f"Error executing procedure {procedure_name}: {err}")
            return None

    # CRUD operations for Players
    def create_player(self, email, password, cosmetic_equipped):
        return self.execute_procedure('create_player', email, password, cosmetic_equipped)

    def get_players(self):
        return self.execute_procedure('get_players_random')

    def update_player(self, player_id, email, password, cosmetic_equipped):
        return self.execute_procedure('update_player', player_id, email, password, cosmetic_equipped)

    def delete_player(self, player_id):
        return self.execute_procedure('delete_player', player_id)

    # CRUD operations for Cosmetics
    def create_cosmetic(self, cosmetic_name, price, version_id):
        return self.execute_procedure('create_cosmetic', cosmetic_name, price, version_id)

    def get_cosmetics(self):
        return self.execute_procedure('get_cosmetics')

    def update_cosmetic(self, cosmetic_id, cosmetic_name, price, version_id):
        return self.execute_procedure('update_cosmetic', cosmetic_id, cosmetic_name, price, version_id)

    def delete_cosmetic(self, cosmetic_id):
        return self.execute_procedure('delete_cosmetic', cosmetic_id)

    # CRUD operations for Weapons
    def create_weapon(self, weapon_name, damage, fire_rate, version_id):
        return self.execute_procedure('create_weapon', weapon_name, damage, fire_rate, version_id)

    def get_weapons(self):
        return self.execute_procedure('get_weapons')

    def update_weapon(self, weapon_id, weapon_name, damage, fire_rate, version_id):
        return self.execute_procedure('update_weapon', weapon_id, weapon_name, damage, fire_rate, version_id)

    def delete_weapon(self, weapon_id):
        return self.execute_procedure('delete_weapon', weapon_id)

    # CRUD operations for Locations
    def create_location(self, location_name, weapons_available_amount, material_available_amount, distance_from_center, version_id):
        return self.execute_procedure('create_location', location_name, weapons_available_amount, material_available_amount, distance_from_center, version_id)

    def get_locations(self):
        return self.execute_procedure('get_locations')

    def update_location(self, location_id, location_name, weapons_available_amount, material_available_amount, distance_from_center, version_id):
        return self.execute_procedure('update_location', location_id, location_name, weapons_available_amount, material_available_amount, distance_from_center, version_id)

    def delete_location(self, location_id):
        return self.execute_procedure('delete_location', location_id)

    # CRUD operations for Updates
    def create_update(self, update_date):
        return self.execute_procedure('create_update', update_date)

    def get_updates(self):
        return self.execute_procedure('get_updates')

    def update_update(self, version_id, update_date):
        return self.execute_procedure('update_update', version_id, update_date)

    def delete_update(self, version_id):
        return self.execute_procedure('delete_update', version_id)

    # CRUD operations for Plays
    def create_play(self, player_id, match_id, kills, time_played, weapon_used, location_visited):
        return self.execute_procedure('create_play', player_id, match_id, kills, time_played, weapon_used, location_visited)

    def get_plays(self):
        return self.execute_procedure('get_plays')

    def update_play(self, player_id, match_id, kills, time_played, weapon_used, location_visited):
        return self.execute_procedure('update_play', player_id, match_id, kills, time_played, weapon_used, location_visited)

    def delete_play(self, player_id, match_id):
        return self.execute_procedure('delete_play', player_id, match_id)

    # CRUD operations for Matches
    def create_match(self, date_played, winner_player_id):
        self.execute_procedure('create_match', date_played, winner_player_id)
        
        # Fetch the last inserted row ID
        match_id = self.cursor.lastrowid

        
        # If lastrowid is 0, fetch the maximum ID from the matches table
        if match_id == 0:
            self.cursor.execute("SELECT MAX(MatchID) FROM `match`")
            match_id = self.cursor.fetchone()[0]

        print(f"Match created with ID: {match_id}")

        
        return match_id


    def get_matches(self):
        return self.execute_procedure('get_matches')

    def update_match(self, match_id, date_played, winner_player_id):
        return self.execute_procedure('update_match', match_id, date_played, winner_player_id)

    def delete_match(self, match_id):
        return self.execute_procedure('delete_match', match_id)

    # CRUD operations for Purchases
    def create_purchase(self, player_id, cosmetic_id, date_purchased):
        return self.execute_procedure('create_purchase', player_id, cosmetic_id, date_purchased)

    def get_purchases(self):
        return self.execute_procedure('get_purchases')

    def delete_purchase(self, player_id, cosmetic_id):
        return self.execute_procedure('delete_purchase', player_id, cosmetic_id)

    # CRUD operations for Friendships
    def create_friendship(self, player_id_1, player_id_2):
        return self.execute_procedure('create_friendship', player_id_1, player_id_2)

    def get_friendships(self):
        return self.execute_procedure('get_friendships')

    def delete_friendship(self, player_id_1, player_id_2):
        return self.execute_procedure('delete_friendship', player_id_1, player_id_2)

def main():
    db_manager = DatabaseManager('localhost', 'root', 'root', 'fortnite')
    db_manager.connect()

if __name__ == "__main__":
    main()
