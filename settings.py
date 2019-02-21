class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed_factor = 2.8
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 2.5
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed_factor_x = 2.5
        self.alien_speed_factor_y = 1
        self.alien_create_rate = 0.98