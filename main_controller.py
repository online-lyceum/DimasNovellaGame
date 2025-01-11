from base_story_controller import *
from main_menu_controller import *


class MainController:
    def __init__(self):
        pass

    def game_loop(self):
        active_story = MainMenuStoryController()
        while not active_story.is_end:
            active_story = active_story.game()

            clock = pygame.time.Clock()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            clock.tick(FPS)
