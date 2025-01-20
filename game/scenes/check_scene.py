import pygame
from pygame import Surface
from pygame.mixer import pause

from game.scenes.new_friends_scene import NewFriendsScene
from game.UI.replicas_loader import ReplicasLoader
from game.UI.storytelling import Storytelling
from game.scenes.base_scene import BaseScene
from game.settings import FPS
from game.UI.blackout import Blackout


class CheckScene(BaseScene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def game(self) -> BaseScene | None:
        loader = ReplicasLoader('./game/replicas/check_scene_script')
        story_listings = []
        for speaker, replica in loader.replicas:
            story_listings.append(Storytelling(speaker, replica))

        for active_story_listing in story_listings:
            while not active_story_listing.is_end:
                clock = pygame.time.Clock()

                self.screen.fill((0, 0, 0))

#                if active_story_listing.speaker == 'pidor':
#                    tioma_o['left-center'].draw(self.screen)
#                if active_story_listing.speaker == 'pidor2':
#                    tioma_b['right-center'].draw(self.screen)

                active_story_listing.draw(self.screen)

                pygame.display.update()

                for event in pygame.event.get():
                    active_story_listing.process_event(event)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                clock.tick(FPS)

        blackout = Blackout(secs=2)     # Затемнение экрана
        blackout.start(self.screen)     #

        return NewFriendsScene(self.screen)
