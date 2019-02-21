import pygame
from pygame.sprite import Group

from settings import Settings
from alien import Alien
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    alien = Alien(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()
    pygame.display.set_caption('Alien Invasion')
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.create_fleet(ai_settings, screen, aliens)
        gf.update_screen(ai_settings, screen, alien, aliens, ship, bullets)

run_game()