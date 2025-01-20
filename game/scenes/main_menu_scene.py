import pygame
from pygame import Surface

from game.media_data import main_menu
from game.scenes.base_scene import BaseScene
from game.scenes.check_scene import CheckScene
from game.settings import FPS
from game.UI.menu import Menu


class MainMenuScene(BaseScene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def game(self) -> BaseScene | None:
        menu = Menu('ШНЯЖНЫЕ', ['Играть', 'Выход'])

        while not menu.selected:
            clock = pygame.time.Clock()
            self.screen.blit(main_menu, (0, 0))
            menu.draw(self.screen)
            pygame.display.update()

            for event in pygame.event.get():
                menu.process_event(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            clock.tick(FPS)

        if menu.selected == 'Играть':
            return CheckScene(self.screen)
        if menu.selected == 'Выход':
            return pygame.quit()
