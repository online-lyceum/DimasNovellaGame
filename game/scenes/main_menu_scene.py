import pygame
from pygame import Surface

from game.scenes.base_scene import BaseScene
from game.scenes.black_scene import BlackScene
from game.settings import FPS
from game.UI.menu import Menu


class MainMenuScene(BaseScene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def game(self) -> BaseScene | None:
        menu = Menu('ШНЯЖНЫЕ', ['Играть', 'Выход'])

        while not menu.selected:
            clock = pygame.time.Clock()
            self.screen.fill((255, 255, 255))
            menu.draw(self.screen)
            pygame.display.update()

            for event in pygame.event.get():
                menu.process_event(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            clock.tick(FPS)

        if menu.selected == 'Играть':
            return BlackScene(self.screen)
        if menu.selected == 'Выход':
            return pygame.quit()
