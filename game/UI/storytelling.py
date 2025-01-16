import pygame
from pygame import Surface

from game.UI import menu
from game.UI.text_box import TextBox
from game.storys_data import story_black


class Storytelling:
    def __init__(self, story: list):
        self.story = story
        self.current_text_index = 0
        self.coords = (200, 800)
        self.text = self.story[self.current_text_index]
        self.surface = pygame.Surface((200, 200))
        self.text_box = TextBox(
            self.text, center=(
                self.surface.get_width(),
                self.surface.get_height()
            )
        )

    def telling(self, on: Surface):
        while True:

            self.text_box.draw(self.surface)
            on.blit(self.surface, self.coords)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.current_text_index += 1
                        if self.current_text_index >= len(self.story):
                            menu.selected = ''

