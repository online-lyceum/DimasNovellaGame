import pygame

from game.stories.main_menu_controller import MainMenuStoryController


class MainController:
    def __init__(self):
        pass

    @staticmethod
    def game_loop():
        active_story = MainMenuStoryController()
        while not active_story.is_end:
            active_story = active_story.game()
            if active_story is None:
                pygame.quit()
                return
