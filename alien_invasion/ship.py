import pygame
from settings import Settings


class Ship:
    """Klasa przeznaczona do zarządzanie statkiem kosmicznym"""

    def __init__(self, ai_game):
        """Inicjalizacja statku kosmicznego"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()

        # Wczytywanie obrazu statku i pobranie jego prostkąta
        self.image = pygame.image.load('images/rocket2.bmp')
        self.rect = self.image.get_rect()

        # Każdy nowy statek pojawia sie na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom

        # Położenie statku jest przechowywane w postaci liczby zmiennoprzecinkowej
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Opcja wskazuje na poruszanie statku
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Uaktualnienie położenia statku"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Wyświetla statek kosmiczny w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """umieszczenie statku na dole ekranu"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
