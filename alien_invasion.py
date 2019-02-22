import pygame
from pygame.sprite import Group

from settings import Settings
from alien import Alien
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    stats = GameStats(ai_settings)
    alien = Alien(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    scoreboard = Scoreboard(ai_settings, screen, stats)
    aliens = Group()
    bullets = Group()
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(ai_settings, screen, 'Play')
    pre_counter = ai_settings.counter
    # Start the main loop for the game.
    while True:
        if ai_settings.counter % ai_settings.level_counter == 0 and pre_counter != ai_settings.counter:
            ai_settings.increase_speed()
            pre_counter = ai_settings.counter

        gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, scoreboard)
        screen.fill(ai_settings.bg_color)
        if stats.game_active:
            gf.create_fleet(ai_settings, screen, aliens)
            ship.update()
            gf.update_bullets(bullets, aliens, stats, ai_settings, scoreboard)
            gf.update_aliens(ai_settings, aliens, ship, bullets, stats)
            gf.update_screen(screen, alien, aliens, ship, scoreboard, ai_settings)
        else:
            play_button.draw_button()
            pygame.display.flip()

run_game()