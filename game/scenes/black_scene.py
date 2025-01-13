import pygame
from pygame import Surface

from game.UI.character import tioma_center
from game.scenes.base_scene import BaseScene
from game.settings import FPS


class BlackScene(BaseScene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def game(self) -> BaseScene | None:
        while True:
            clock = pygame.time.Clock()
            self.screen.fill((250, 150, 150))
            tioma_center.draw(self.screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            clock.tick(FPS)
