import pygame

from game.main_menu_controller import MainMenuStoryController
from game.settings import FPS


class MainController:
    def __init__(self):
        pass

    @staticmethod
    def game_loop():
        active_story = MainMenuStoryController()
        while not active_story.is_end:
            active_story = active_story.game()

            clock = pygame.time.Clock()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            clock.tick(FPS)
