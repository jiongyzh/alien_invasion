class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, settings):
        self.settings = settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit