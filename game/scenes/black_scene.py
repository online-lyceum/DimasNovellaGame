import pygame
from pygame import Surface

from game.UI.character import tioma_o, tioma_b
from game.UI.backgrounds import mahutov_room
from game.UI.storytelling import Storytelling
from game.scenes.base_scene import BaseScene
from game.settings import FPS
from game.storys_data import *

class BlackScene(BaseScene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def game(self) -> BaseScene | None:
        story_1 = Storytelling(story_black_1)
        while not story_1.is_end:
            clock = pygame.time.Clock()

            mahutov_room.draw(self.screen)
            tioma_o['left-center'].draw(self.screen)
            story_1.draw(self.screen)

            pygame.display.update()

            for event in pygame.event.get():
                story_1.process_event(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            clock.tick(FPS)

        from game.scenes.main_menu_scene import MainMenuScene
        return MainMenuScene(self.screen)
