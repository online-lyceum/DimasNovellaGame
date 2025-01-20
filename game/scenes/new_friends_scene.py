import pygame
from pygame import Surface

from game.scenes.base_scene import BaseScene
from game.scenes.server_room import secret_server_room_event_process
from game.scenes.server_room import ServerRoomScene
from game.settings import FPS
from game.UI.backgrounds import mahutov_room
from game.UI.blackout import Blackout
from game.UI.replicas_loader import ReplicasLoader
from game.UI.storytelling import Storytelling
from game.UI.character import tioma_b


class NewFriendsScene(BaseScene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def game(self):
        loader = ReplicasLoader('./game/replicas/new_friends_scene_script')
        story_listings = []
        for speaker, replica in loader.replicas:
            story_listings.append(Storytelling(speaker, replica))

        for active_story_listing in story_listings:
            while not active_story_listing.is_end:
                clock = pygame.time.Clock()

                mahutov_room.draw(self.screen)

                tioma_b['center'].draw(self.screen)

                active_story_listing.draw(self.screen)

                pygame.display.update()

                for event in pygame.event.get():
                    active_story_listing.process_event(event)
                    if secret_server_room_event_process(event):
                        blackout = Blackout(secs=2)
                        blackout.start(self.screen)
                        return ServerRoomScene(self.screen)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                clock.tick(FPS)

        from game.scenes.main_menu_scene import MainMenuScene
        return MainMenuScene(self.screen)
