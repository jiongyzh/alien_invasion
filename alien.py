import pygame
from pygame.sprite import Sprite
from random import randint
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

    def blit_me(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien."""
        if self.rect.right >= self.screen.get_rect().right:
            self.x -= self.settings.alien_speed_factor_x
            self.direction_flag = False
        elif self.rect.left <= 0:
            self.x += self.settings.alien_speed_factor_x
            self.direction_flag = True
        elif self.change_direction_flag:
            if random() - 0.5 > 0:
                self.x += self.settings.alien_speed_factor_x
                self.direction_flag = True
            else:
                self.x -= self.settings.alien_speed_factor_x
                self.direction_flag = False
        elif not self.change_direction_flag:
            if self.direction_flag:
                self.x += self.settings.alien_speed_factor_x
            else:
                self.x -= self.settings.alien_speed_factor_x
        self.change_direction_flag = False


        self.y += self.settings.alien_speed_factor_y

        self.rect.x = self.x
        self.rect.y = self.y