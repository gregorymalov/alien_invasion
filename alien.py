import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс для управления короблей пришельцев"""

    def __init__(self, ai_game):
        """Инициализация прешельца"""
        super().__init__()
        self.screen = ai_game.screen

        #Загружаем картинку
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        #Каждый новый пришелец появляетсяв левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
