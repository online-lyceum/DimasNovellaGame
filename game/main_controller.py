import pygame

from game.scenes.base_scene import BaseScene


class MainController:
    def __init__(self):
        pass

    @staticmethod
    def game_loop(active_story: BaseScene):
        while not active_story.is_end:
            active_story = active_story.game()
            if active_story is None:
                pygame.quit()
                return