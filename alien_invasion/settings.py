class Settings:
    """klasa przeznaczona do przechowywania ustawień gry"""

    def __init__(self):
        """Inicjalizacja ustawień gry"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 204, 255)
        self.ship_speed = 1.2
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
