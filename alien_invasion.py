import pygame
from pygame.sprite import Group

from settings import Settings
from alien import Alien
from ship import Ship
from game_stats import GameStats
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    stats = GameStats(ai_settings)
    alien = Alien(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()
    pygame.display.set_caption('Alien Invasion')
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.create_fleet(ai_settings, screen, aliens)
        screen.fill(ai_settings.bg_color)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens)
            gf.update_aliens(aliens, ship, bullets, stats)
            gf.update_screen(screen, alien, aliens, ship)

run_game()