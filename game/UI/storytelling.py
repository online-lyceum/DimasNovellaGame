import pygame
from pygame import Surface
from pygame.event import Event

from game.UI import menu
from game.UI.text_box import TextBox


class Storytelling:
    def __init__(self, speaker: str, story: list[str]):
        self.speaker = speaker
        self.story = story
        self.current_text_index = 0
        self.coords = (460, 800)
        self.ticks_count = 0
        self.is_end = False

    def draw(self, on: Surface):
        self.ticks_count += 1
        text_box_title = TextBox(
            self.speaker, left_top=(
                10,
                10
            )
        )
        text_box_text = TextBox(
            self.story[self.current_text_index][:self.ticks_count // 2], left_top=(
                10,
                60
            )
        )
        surface = pygame.Surface((1000, 250))
        text_box_title.draw(surface)
        text_box_text.draw(surface)
        on.blit(surface, self.coords)

    def process_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.current_text_index += 1
                self.ticks_count = 0
                if self.current_text_index >= len(self.story):
                    self.is_end = True

