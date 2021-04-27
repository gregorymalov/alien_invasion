class Settings():
    """Класс для хранения всех настроек игры."""

    def __init__(self):
        """Инициализация настройки игры."""
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 1000
        self.bg_color = (0, 0, 0)
        
        #Настройка скорости коробля
        self.ship_speed = 1.5

        #Настройка скорости коробля
        self.alien_speed = 1.5

        #Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3