import pygame

from game.scenes.base_scene import BaseSceneController
from game.settings import FPS
from main import screen


class BlackSceneController(BaseSceneController):
    def __init__(self):
        super().__init__()

    def game(self) -> BaseSceneController | None:
        while True:
            clock = pygame.time.Clock()
            screen.fill((0, 0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            clock.tick(FPS)
