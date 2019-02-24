import sys
import pygame
from random import random
from random import randint
from pygame.mixer import Sound

from bullet import Bullet
from alien import Alien


def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < settings.bullets_allowed:
        play_sound('shot.wav')
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_event(event, settings, screen, ship, bullets, stats):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        if stats.game_active:
            fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        if stats.score > stats.pre_high_score:
            record_highest_score(stats)
        sys.exit()


def check_keyup_event(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(settings, screen, ship, bullets, play_button, stats, scoreboard):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, settings, screen, ship, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, settings, screen, ship, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, stats, play_button, mouse_x, mouse_y, scoreboard)


def update_bullets(bullets, aliens, stats, settings, scoreboard):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 12:
            bullets.remove(bullet)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    if pygame.sprite.groupcollide(bullets, aliens, True, True):
        play_sound('boom.wav')
        stats.score += settings.alien_points
        stats.shoot_alient_number += 1
        scoreboard.prep_ships(settings)
        scoreboard.prep_score()

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()


def update_screen(screen, alien, aliens, ship, scoreboard, settings):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    alien.blit_me()
    ship.blit_me()
    aliens.draw(screen)
    scoreboard.prep_level(settings)
    scoreboard.prep_ships(settings)
    scoreboard.show_score()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def create_fleet(settings, screen, aliens):
    """Create a fleet of aliens."""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    aa = random()
    if aa > settings.alien_create_rate:
        slot_number_x = settings.screen_width // alien_width
        slot_number_y = settings.screen_height / 2 // alien_height
        alien.x = alien_width * randint(0, slot_number_x)
        alien.y = alien_height * randint(0, slot_number_y)
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        if alien.rect.right > screen.get_rect().right:
            alien.straight_flag = False
        aliens.add(alien)
        settings.counter += 1


def update_aliens(settings, aliens, ship, bullets, stats, scoreboard):
    """Update the postions of all aliens in the fleet."""
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, aliens, ship, bullets, stats, scoreboard)

    check_aliens_bottom(settings, aliens, ship, bullets, stats, scoreboard)


def ship_hit(settings, aliens, ship, bullets, stats, scoreboard):
    """Respond to ship being hit by alien."""
    play_sound('crash.wav')
    if stats.ships_left > 1:
        stats.ships_left -= 1
        bullets.empty()
        ship.center_ship()
        scoreboard.prep_ships(settings)
    else:
        if stats.score > stats.pre_high_score:
            record_highest_score(stats)

        stats.game_active = False
        aliens.empty()
        bullets.empty()
        ship.center_ship()
        pygame.mouse.set_visible(True)
        settings.counter = 1


def check_aliens_bottom(settings, aliens, ship, bullets, stats, scoreboard):
    for alien in aliens.sprites():
        if alien.rect.bottom > alien.screen.get_rect().bottom:
            ship_hit(settings, aliens, ship, bullets, stats, scoreboard)
            aliens.remove(alien)


def check_play_button(settings, stats, play_button, mouse_x, mouse_y, scoreboard):
    """Start a new game when the player clicks Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        play_sound('fight.wav')
        pygame.mouse.set_visible(False)
        stats.game_active = True
        stats.reset_stats()
        settings.initialize_dynamic_settings()
        scoreboard.prep_high_score()
        scoreboard.prep_score()
        scoreboard.prep_level(settings)
        scoreboard.prep_ships(settings)


def record_highest_score(stats):
    with open('record.txt', 'w') as record_file:
        try:
            record_file.write(str(stats.score))
        except ValueError:
            pass


def play_sound(sound_name):
    sound = 'sounds/{}'.format(sound_name)
    try:
        Sound(sound).play()
    except FileNotFoundError:
        pass

