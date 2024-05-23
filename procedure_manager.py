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
                result_sets = [result.fetchall() for result in

                self.cursor.stored_results()]
                self.connection.commit()
                return result_sets
            except mysql.connector.Error as err:
                print(f"Error executing procedure {procedure_name}: {err}")
                return None
            # CRUD operations for Players
    def create_player(self, password, currently_equipped):
        return self.execute_procedure('create_player', password,
        currently_equipped)
    def get_players(self):
        return self.execute_procedure('get_players')
    def update_player(self, player_id, password, currently_equipped):
        return self.execute_procedure('update_player', player_id, password,
        currently_equipped)
    def delete_player(self, player_id):
        return self.execute_procedure('delete_player', player_id)
    # CRUD operations for Cosmetics
    def create_cosmetic(self, cosmetic_name, cosmetic_type, price):

        return self.execute_procedure('create_cosmetic', cosmetic_name,
        cosmetic_type, price)
    def get_cosmetics(self):
        return self.execute_procedure('get_cosmetics')
    def update_cosmetic(self, cosmetic_id, cosmetic_name, cosmetic_type,
    price):
        return self.execute_procedure('update_cosmetic', cosmetic_id,
    cosmetic_name, cosmetic_type, price)
    def delete_cosmetic(self, cosmetic_id):
        return self.execute_procedure('delete_cosmetic', cosmetic_id)
    # CRUD operations for Weapons
    def create_weapon(self, damage, fire_rate):
        return self.execute_procedure('create_weapon', damage, fire_rate)
    def get_weapons(self):
        return self.execute_procedure('get_weapons')
    def update_weapon(self, weapon_id, damage, fire_rate):
        return self.execute_procedure('update_weapon', weapon_id, damage,
        fire_rate)
    def delete_weapon(self, weapon_id):
        return self.execute_procedure('delete_weapon', weapon_id)
    # CRUD operations for Locations
    def create_location(self, weapons_available, material_available,
    distance_from_center):
        return self.execute_procedure('create_location', weapons_available,
    material_available, distance_from_center)
    def get_locations(self):
        return self.execute_procedure('get_locations')
    def update_location(self, location_id, weapons_available,
    material_available, distance_from_center):
        return self.execute_procedure('update_location', location_id,
    weapons_available, material_available, distance_from_center)
    def delete_location(self, location_id):
        return self.execute_procedure('delete_location', location_id)
    # CRUD operations for Updates

    def create_update(self, newly_added_locations, newly_added_weapons,
    newly_added_cosmetics, shop_schedule, locations_balanced, weapons_balanced,
    update_date):
        return self.execute_procedure('create_update', newly_added_locations,
    newly_added_weapons, newly_added_cosmetics, shop_schedule, locations_balanced,
    weapons_balanced, update_date)
    def get_updates(self):
        return self.execute_procedure('get_updates')
    def update_update(self, update_id, newly_added_locations,
    newly_added_weapons, newly_added_cosmetics, shop_schedule, locations_balanced,
    weapons_balanced, update_date):
        return self.execute_procedure('update_update', update_id,
    newly_added_locations, newly_added_weapons, newly_added_cosmetics,
    shop_schedule, locations_balanced, weapons_balanced, update_date)
    def delete_update(self, update_id):
        return self.execute_procedure('delete_update', update_id)
    # CRUD operations for Plays
    def create_play(self, player_id, weapon_id, location_id, enemies_killed,
    time_played):
        return self.execute_procedure('create_play', player_id, weapon_id,
    location_id, enemies_killed, time_played)
    def get_plays(self):
        return self.execute_procedure('get_plays')
    def update_play(self, play_id, player_id, weapon_id, location_id,
    enemies_killed, time_played):
        return self.execute_procedure('update_play', play_id, player_id,
    weapon_id, location_id, enemies_killed, time_played)
    def delete_play(self, play_id):
        return self.execute_procedure('delete_play', play_id)
    # CRUD operations for Matches
    def create_match(self, play_id, winner_player_id, date_played):
        return self.execute_procedure('create_match', play_id,
    winner_player_id, date_played)
    def get_matches(self):
        return self.execute_procedure('get_matches')

    def update_match(self, match_id, play_id, winner_player_id, date_played):
        return self.execute_procedure('update_match', match_id, play_id,
    winner_player_id, date_played)
    def delete_match(self, match_id):
        return self.execute_procedure('delete_match', match_id)
    # CRUD operations for Purchases
    def create_purchase(self, player_id, cosmetic_id):
        return self.execute_procedure('create_purchase', player_id,
    cosmetic_id)
    def get_purchases(self):
        return self.execute_procedure('get_purchases')
    def delete_purchase(self, player_id, cosmetic_id):
        return self.execute_procedure('delete_purchase', player_id,
    cosmetic_id)
    # CRUD operations for Friends
    def create_friend(self, player_id_1, player_id_2):
        return self.execute_procedure('create_friend', player_id_1,
    player_id_2)
    def get_friends(self):
        return self.execute_procedure('get_friends')
    def delete_friend(self, player_id_1, player_id_2):
        return self.execute_procedure('delete_friend', player_id_1,
    player_id_2)

def main():
    db_manager = DatabaseManager('localhost', 'root', 'root', 'fortnite')
    db_manager.connect()

if __name__ == "__main__":
    main()