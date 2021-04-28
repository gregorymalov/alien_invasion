import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс для управления короблей пришельцев"""

    def __init__(self, ai_game):
        """Инициализация прешельца"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Загружаем картинку
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        #Каждый новый пришелец появляетсяв левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращает True, если пришелец находиться у края"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Перемещает пришельца в право"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
