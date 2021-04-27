import pygame

class Ship():
    """Модуль коробля"""
    def __init__(self, ai_game):
        """Инициализируем корабль и задаём начальную позицию"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Загружаем картинку
        self.image = pygame.image.load('images/ship.gif')
        self.rect = self.image.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        #Сохранение вещественной координаты центра коробля.
        self.x = float(self.rect.x)

        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        #Обновляем атрибут x, не rect
        if self.moving_right and self.rect.right  <  self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left  >  0:
            self.x -= self.settings.ship_speed

        #Обновление атрибута rect на основании self.x
        self.rect.x = self.x
    

    def blitme(self):
        """Рисуем корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
