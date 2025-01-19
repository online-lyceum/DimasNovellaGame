import pygame
from pygame import Surface

from game.UI.character import tioma_o, tioma_b
from game.UI.backgrounds import mahutov_room
from game.UI.replicas_loader import ReplicasLoader
from game.UI.storytelling import Storytelling
from game.scenes.base_scene import BaseScene
from game.settings import FPS


class BlackScene(BaseScene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def game(self) -> BaseScene | None:
        loader = ReplicasLoader('./game/replicas/black_story')
        story_listings = []
        for speaker, replica in loader.replicas:
            story_listings.append(Storytelling(speaker, replica))

        for active_story_listing in story_listings:
            while not active_story_listing.is_end:
                clock = pygame.time.Clock()

                mahutov_room.draw(self.screen)

                if active_story_listing.speaker == 'pidor':
                    tioma_o['left-center'].draw(self.screen)
                if active_story_listing.speaker == 'pidor2':
                    tioma_b['right-center'].draw(self.screen)

                active_story_listing.draw(self.screen)

                pygame.display.update()

                for event in pygame.event.get():
                    active_story_listing.process_event(event)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                clock.tick(FPS)

        from game.scenes.main_menu_scene import MainMenuScene
        return MainMenuScene(self.screen)
