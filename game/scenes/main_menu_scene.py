import pygame

from game.scenes.base_scene import BaseSceneController
from game.scenes.black_scene import BlackSceneController
from game.settings import FPS
from game.settings import HEIGHT
from game.settings import WIDTH
from game.UI.menu import Menu

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN)


class MainMenuSceneController(BaseSceneController):
    def __init__(self):
        super().__init__()

    def game(self) -> BaseSceneController | None:
        menu = Menu('привет', ['играть', 'пока'])

        while not menu.selected:
            clock = pygame.time.Clock()
            screen.fill((255, 255, 255))
            menu.draw(screen)
            pygame.display.update()

            for event in pygame.event.get():
                menu.process_event(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            clock.tick(FPS)

        if menu.selected == '':
            return MainMenuSceneController()
        if menu.selected == 'играть':
            return BlackSceneController()
        if menu.selected == 'пока':
            return pygame.quit()
