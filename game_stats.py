class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, settings):
        self.settings = settings
        self.game_active = False
        self.high_score = 0
        self.reset_stats()
        self.get_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.add_ship_number = 0
        self.shoot_alient_number = 0

    def get_high_score(self):
        try:
            with open('record.txt', 'r') as record_file:
                try:
                    self.high_score = int(record_file.read().strip())
                except ValueError:
                    self.high_score = 0
        except FileNotFoundError:
            self.high_score = 0

        self.pre_high_score = self.high_score
