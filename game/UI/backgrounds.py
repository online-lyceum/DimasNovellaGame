import pygame

from pygame import Surface
from game.media_data import *


class Background:
    def __init__(self, image):
        self.cords = (0, 0)
        self.image = image

    def draw(self, on: Surface):
        on.blit(self.image, self.cords)


mahutov_room = Background(m_room)

