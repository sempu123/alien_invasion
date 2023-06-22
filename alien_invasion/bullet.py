import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Klasa przeznaczona do ządzania pociskami """

    def __init__(self, ai_game):
        """Utworzenie obiektu pocisku w akutaalnym położeniu statku"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Utworzenie pocisku w punkcie (0, 0) a nasstępnie
        # zdefiniowanie dla niego położenia
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Poruszanie pociskiem"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Wyswietla pocisk na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)
