import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Klasa do zarządzania kosmitą"""

    def __init__(self, ai_game):
        """Inicjalizacja kosmity """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # wczytanie obrazu obcego i nadanie mu atrybutu rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # umieszczenie nowego obcego w górnym prawym rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Zwraca wartość True, jeśli obcy jest przy krawędzi ekrany"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """przesuwa obcego w prawo"""
        self.x += self.settings.alien_speed * self.settings.fleet_directions
        self.rect.x = self.x
