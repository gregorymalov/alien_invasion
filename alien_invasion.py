import sys
import pygame

class AlienInvasion:
    """"Управление ресурами игры."""

    def __init__(self):
        """"Инициализация игры."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230,230,230)
    
    def run_game(self):
        """"Запуск нового цикла игры."""
        while True:
            #Отслеживаем события клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            #Отображение последнего прорисованного экрана.
            pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()





