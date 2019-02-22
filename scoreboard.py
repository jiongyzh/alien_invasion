import pygame.ftfont as font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.pre_shoot_alient_number = 0

        self.text_color = (30, 30, 30)
        self.font = font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level(settings)
        self.prep_ships(settings)

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = '{:,}'.format(int(round(self.stats.score)))
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score_str = 'RECORD: {:,}'.format(int(round(self.stats.high_score)))
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self, settings):
        """Turn the high score into a rendered image."""
        level_str = 'LEVEL: {}'.format(int(round(self.stats.level + settings.counter // settings.level_counter)))
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom

    def prep_ships(self, settings):
        """Show how many ships are left."""
        if self.stats.shoot_alient_number == settings.alien_numbers_for_one_ship * (1 + self.stats.add_ship_number):
            if self.pre_shoot_alient_number != self.stats.shoot_alient_number and \
                            self.stats.ships_left < settings.max_ship_number:
                self.stats.ships_left += 1
                self.stats.add_ship_number += 1
                self.pre_shoot_alient_number = self.stats.shoot_alient_number
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.settings, self.screen)
            ship.rect.x = ship_number * ship.rect.width + 10
            ship.rect.top = ship.screen_rect.top
            self.ships.add(ship)

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
