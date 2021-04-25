import pygame

class Ship():
    """Модуль коробля"""
    def __init__(self, ai_game):
        """Инициализируем корабль и задаём начальную позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Загружаем картинку
        self.image = pygame.image.load('images/ship.gif')
        self.rect = self.image.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
    

    def blitme(self):
        """Рисуем корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
