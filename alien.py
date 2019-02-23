import pygame
from pygame.sprite import Sprite
from random import random


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.direction_flag = True
        self.change_direction_flag = True
        if random() > 0.2:
            self.straight_flag = False
        else:
            self.straight_flag = True
        if random() > 0.95:
            self.alien_speed_factor_x = self.settings.alien_speed_factor_x * 3
            self.alien_speed_factor_y = self.settings.alien_speed_factor_y * 1.2
        elif random() > 0.9:
            self.alien_speed_factor_x = self.settings.alien_speed_factor_x * 2
            self.alien_speed_factor_y = self.settings.alien_speed_factor_y * 1.2
        elif random() > 0.75:
            self.alien_speed_factor_x = self.settings.alien_speed_factor_x * 1.5
            self.alien_speed_factor_y = self.settings.alien_speed_factor_y * 1.1
        else:
            self.alien_speed_factor_x = self.settings.alien_speed_factor_x
            self.alien_speed_factor_y = self.settings.alien_speed_factor_y

    def blit_me(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien."""

        if not self.straight_flag:
            if self.rect.right >= self.screen.get_rect().right:
                self.x -= self.alien_speed_factor_x
                self.direction_flag = False
            elif self.rect.left <= 0:
                self.x += self.alien_speed_factor_x
                self.direction_flag = True
            elif self.change_direction_flag:
                if random() > 0.5:
                    self.x += self.alien_speed_factor_x
                    self.direction_flag = True
                else:
                    self.x -= self.alien_speed_factor_x
                    self.direction_flag = False
            elif not self.change_direction_flag:
                if self.direction_flag:
                    self.x += self.alien_speed_factor_x
                else:
                    self.x -= self.alien_speed_factor_x
        self.change_direction_flag = False

        self.y += self.alien_speed_factor_y

        self.rect.x = self.x
        self.rect.y = self.y