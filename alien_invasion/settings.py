class Settings:
    """klasa przeznaczona do przechowywania ustawień gry"""

    def __init__(self):
        """Inicjalizacja ustawień gry"""
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (0, 204, 255)
        self.ship_speed = 1.2
        self.ship_limit = 3
        self.bullet_speed = 2.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # jeżeli kierunek jest = 1 to oznacza prawo jeśli -1 oznacza lewo
        self.fleet_directions = 1

