import pygame
from pygame import Surface
from pygame.event import Event

from game.UI import menu
from game.UI.text_box import TextBox
from game.storys_data import *


class Storytelling:
    def __init__(self, story: tuple):
        self.story = story
        self.current_text_index = 0
        self.coords = (460, 800)
        self.is_end = False

    def draw(self, on: Surface):
        text_box = TextBox(
            self.story[self.current_text_index], left_top=(
                10,
                10
            )
        )
        surface = pygame.Surface((1000, 250))
        text_box.draw(surface)
        on.blit(surface, self.coords)

    def process_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.current_text_index += 1
                if self.current_text_index >= len(self.story):
                    self.is_end = True

