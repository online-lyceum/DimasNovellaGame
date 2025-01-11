import pygame
from pygame import Surface

from game.UI.text_box import TextBox


class Button:
    def __init__(
            self,
            text: str,
            coords: tuple[int, int],
            width=200,
            height=100
    ):
        self.width = width
        self.height = height
        self.coords = coords
        self.rect = pygame.Rect(*coords, width, height)
        self.surface = pygame.Surface((width, height))
        self.text_box = TextBox(
            text, center=(
                self.surface.get_width() // 2,
                self.surface.get_height() // 2
            )
        )

    def draw(self, on: Surface):
        self.text_box.draw(self.surface)
        on.blit(self.surface, self.coords)
