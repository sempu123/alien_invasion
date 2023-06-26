import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


class AlienInvasion:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposbem działania gry """

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Inwazja Obcych")

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Rozpoczęcie pętli i głownej gry"""

        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self.update_aliens()
            self.update_screen()

    def _check_events(self):
        """Reakcja na zdarzenia generowanie przez klawiaturę i mysz"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyups_event(event)

    def _check_keydown_event(self, event):
        """Reakcja na naciśnięty klawisz"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyups_event(self, event):
        """Reakcja na zwolnienia klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """utworzenie nowego pocisku"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            # noinspection PyTypeChecker
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Aktualizacja położenia pocisków"""
        self.bullets.update()

        # Usunięcie pocisków
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        """Zminijszenie posiadanych statków"""
        if self.stats.game_active > 0:
            self.stats.ship_left -= 1

            # usunięcie alienów i pocisków
            self.aliens.empty()
            self.bullets.empty()

            self.ship.center_ship()
            # przerwa
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_bullet_alien_collision(self):
        """sprawdza colizje miedzy alienem a pociskiem"""
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def update_aliens(self):
        """Uaktualnia pozycje aliena"""
        self._check_fleet_edges()
        self.aliens.update()

        # Wykrywanie kolizji miedzy statkiem a obcym
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _create_fleet(self):
        """Tworzy flotę obcych"""
        # Tworzy obcego oraz ustala ilu się zmieści
        # odległość między obcymi
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # ustalenie ile rzedów się zmiści
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (4 * alien_height) - ship_height)
        number_of_rows = available_space_y // (2 * alien_height)

        # stworzenie pierwszego rzędu
        for row_number in range(number_of_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # utworzenie i umieszczenie go w rzędzie
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Odpowiednia reakcja gdy flota dotrze do krawedzi ekranu"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """przesuwa cała flotę w dół i zminia jej kierunek"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_directions *= -1

    def _check_aliens_bottom(self):
        """sprawdza czy jakis obcy doleciał do dolnego ekranu"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def update_screen(self):
        """Uaktualnienie obrazów na ekranie i przescie do nowego"""
        # odświeżenie ekranu w trakcie kazdej iteracji pętli
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Wyświetlanie ostatnio zmodyfikowanego ekranu
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
