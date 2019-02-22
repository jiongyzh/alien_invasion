class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1000
        self.screen_height = 750
        self.bg_color = (230, 230, 230)
        self.level_counter = 20
        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # Alien settings
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 4
        self.bullet_speed_factor = 5
        self.alien_speed_factor_x = 2
        self.alien_speed_factor_y = 0.6
        self.alien_create_rate = 0.98
        self.alien_points = 1
        self.counter = 0

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor_x *= self.speedup_scale
        self.alien_speed_factor_y *= self.speedup_scale
        self.alien_create_rate -= 0.001
        self.alien_points *= self.speedup_scale
