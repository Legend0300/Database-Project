from faker import Faker
import random

class DatabaseFaker:
    def __init__(self, db_manager):
        self.fake = Faker()
        self.db_manager = db_manager

    def create_player(self, num_players):
        try:
            for _ in range(num_players):
                username = self.fake.unique.user_name()
                password = self.fake.password()
                cosmetic_equipped = random.randint(1, 4)  # Assuming cosmetic IDs start from 1 to 10
                self.db_manager.create_player(username, password, cosmetic_equipped)
        except Exception as e:
            print(f"Error creating players: {e}")

    def load_players(self):
        try:
            return self.db_manager.get_players()
        except Exception as e:
            print(f"Error loading players: {e}")
            return []

    def create_match(self):
        try:
            match_date = self.fake.date_time_between(start_date="-1y", end_date="now")
            players = self.load_players()[0]
            #count players and print them
            # print(f"Players: {players}")
            winner_player_id = random.choice([player[0] for player in players])
            print(f"Winner Player ID: {winner_player_id}")
            match_id = self.db_manager.create_match(match_date, winner_player_id)
            if players:
                total_kills = 100
                for player in players:
                    player_id = player[0]
                    kills = random.randint(0, total_kills)
                    total_kills -= kills
                    time_played = self.fake.time(pattern="%H:%M:%S", end_datetime="-1d")
                    weapon_used = random.randint(1, 4)  # Assuming weapon IDs start from 1 to 10
                    location_visited = random.randint(1, 3)  # Assuming location IDs start from 1 to 10
                    self.db_manager.create_play(player_id, match_id, kills, time_played, weapon_used, location_visited)
        except Exception as e:
            print(f"Error creating match: {e}")

    def create_matches(self, num_matches):
        try:
            for _ in range(num_matches):
                self.create_match()
        except Exception as e:
            print(f"Error creating matches: {e}")
