from math import sqrt

import pygame
from pygame import Surface

from game.settings import FPS
from game.settings import HEIGHT
from game.settings import WIDTH


class Blackout:
    def __init__(
            self,
            color: tuple[int, int, int] = (0, 0, 0),
            secs: float = 1
    ):
        self._color = color
        self._total_ticks = int(FPS * secs)
        self._ticks = 0

    def start(self, on: Surface):
        clock = pygame.time.Clock()
        for i in range(self._total_ticks):
            self.draw(on)
            pygame.display.update()
            clock.tick(FPS)

    @property
    def is_end(self):
        return self._ticks >= self._total_ticks

    def reset(self):
        self._ticks = 0

    def draw(self, on: Surface):
        if self._ticks >= self._total_ticks:
            return
        self._ticks += 1
        alpha: float = 255 - sqrt(
            255 ** 2 * (
                    self._total_ticks - self._ticks) ** 2 / self._total_ticks ** 2
        )
        surface = Surface((WIDTH, HEIGHT))
        surface.set_alpha(int(alpha))
        surface.fill(self._color)
        on.blit(
            surface,
            (0, 0)
        )

    def reverse_draw(self, on: Surface):
        if self._ticks >= self._total_ticks:
            return
        self._ticks += 1
        alpha: float = 255 - sqrt(
            255 ** 2 * self._ticks ** 2 / self._total_ticks ** 2
        )
        surface = Surface((WIDTH, HEIGHT))
        surface.set_alpha(int(alpha))
        surface.fill(self._color)
        on.blit(
            surface,
            (0, 0)
        )
