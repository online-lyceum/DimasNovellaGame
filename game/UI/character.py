import pygame
from pygame import Surface

from game.media_data import t_0, t_b

coords = {
    'left': (110, 280),
    'left-center': (400, 280),
    'center': (710, 280),
    'right-center': (1000, 280),
    'right': (1310, 280)
}

class Character:
    def __init__(self, name, texture, pos):
        self.name = name
        self.texture = texture
        self.pos = pos

    def draw(self, on: Surface):
        on.blit(self.texture, self.pos)


tioma_0 = {
    'left': Character('Тёма', t_0, coords['left']),
    'left-center': Character('Тёма', t_0, coords['left-center']),
    'center': Character('Тёма', t_0, coords['center']),
    'right-center': Character('Тёма', t_0, coords['right-center']),
    'right': Character('Тёма', t_0, coords['right'])
}

tioma_b = {
    'left': Character('Тёма', t_b, coords['left']),
    'left-center': Character('Тёма', t_b, coords['left-center']),
    'center': Character('Тёма', t_b, coords['center']),
    'right-center': Character('Тёма', t_b, coords['right-center']),
    'right': Character('Тёма', t_b, coords['right'])
}
