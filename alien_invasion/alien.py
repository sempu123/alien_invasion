import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Klasa do zarządzania kosmitą"""

    def __init__(self, ai_game):
        """Inicjalizacja kosmity """
        super().__init__()
        self.screen = ai_game.screen

        # wczytanie obrazu obcego i nadanie mu atrybutu rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # umieszczenie nowego obcego w górnym prawym rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

