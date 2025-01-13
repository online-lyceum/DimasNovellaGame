import pygame
from pygame import Surface

from game.media_data import t_0

coords = {
    'left': (210, 280),
    'left-center': (0, 280),
    'center': (710, 280),
    'right-center': (0, 280),
    'right': (0, 280)
}

class Character:
    def __init__(self, name, texture, pos):
        self.name = name
        self.texture = texture
        self.pos = pos

    def draw(self, on: Surface):
        on.blit(self.texture, self.pos)


tioma_center = Character('Тёма', t_0, coords['center'])

