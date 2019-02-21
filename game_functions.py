import sys
import pygame
from random import random
from random import randint
from time import sleep

from bullet import Bullet
from alien import Alien


def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_event(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
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


def check_events(settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, settings, screen, ship, bullets)


def update_bullets(bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 12:
            bullets.remove(bullet)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    pygame.sprite.groupcollide(bullets, aliens, True, True)


def update_screen(screen, alien, aliens, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    alien.blit_me()
    ship.blit_me()
    aliens.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def create_fleet(settings, screen, aliens):
    """Create a fleet of aliens."""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    if random() > settings.alien_create_rate:
        slot_number_x = settings.screen_width // alien_width
        slot_number_y = settings.screen_height / 2 // alien_height
        alien.x = alien_width * randint(0, slot_number_x)
        alien.y = alien_height * randint(0, slot_number_y)
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        aliens.add(alien)


def update_aliens(aliens, ship, bullets, stats):
    """Update the postions of all aliens in the fleet."""
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ship, bullets, stats)

    check_aliens_bottom(aliens, ship, bullets, stats)


def ship_hit(ship, bullets, stats):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 1:
        stats.ships_left -= 1
        bullets.empty()
        ship.center_ship()
    else:
        stats.game_active = False


def check_aliens_bottom(aliens, ship, bullets, stats):
    for alien in aliens.sprites():
        if alien.rect.bottom > alien.screen.get_rect().bottom:
            ship_hit(ship, bullets, stats)
            aliens.remove(alien)

