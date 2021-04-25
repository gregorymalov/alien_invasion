import sys
import pygame
from settings import Settings

class AlienInvasion:
    """"Управление ресурами игры."""

    def __init__(self):
        """"Инициализация игры."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """"Запуск нового цикла игры."""
        while True:
            #Отслеживаем события клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Меняем фон
            self.screen.fill(self.settings.bg_color)

            #Отображение последнего прорисованного экрана.
            pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()





