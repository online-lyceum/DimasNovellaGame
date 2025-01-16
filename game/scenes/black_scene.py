import pygame
from pygame import Surface

from game.UI.character import tioma_o, tioma_b
from game.UI.backgrounds import mahutov_room
from game.scenes.base_scene import BaseScene
from game.settings import FPS


class BlackScene(BaseScene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def game(self) -> BaseScene | None:
        while True:
            clock = pygame.time.Clock()
            self.screen.fill((250, 150, 150))
            mahutov_room.draw(self.screen)
            tioma_b['left-center'].draw(self.screen)
            tioma_o['right-center'].draw(self.screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            clock.tick(FPS)
