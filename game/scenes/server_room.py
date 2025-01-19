import pygame
from pygame.event import Event

from game.UI.blackout import Blackout
from game.UI.character import tioma_o, tioma_b
from game.UI.backgrounds import mahutov_room
from game.UI.storytelling import Storytelling
from game.scenes.base_scene import BaseScene
from game.settings import FPS
from game.storys_data import *


secret_key = pygame.K_k

def secret_server_room_event_process(event: Event) -> bool:
    return event.type == pygame.KEYDOWN and event.key == secret_key


class ServerRoomScene(BaseScene):
    def game(self) -> BaseScene | None:
        story_1 = Storytelling(story_black_1)
        blackout = Blackout(secs=1)
        clock = pygame.time.Clock()
        while not blackout.is_end:
            self.screen.fill('red')
            blackout.reverse_draw(self.screen)
            pygame.display.update()
        while not story_1.is_end:
            self.screen.fill('red')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            clock.tick(FPS)

        from game.scenes.main_menu_scene import MainMenuScene
        return MainMenuScene(self.screen)
