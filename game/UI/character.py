import pygame


from game.media_data import t_0
from game.settings import HEIGHT
from game.settings import WIDTH

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN)

class Character:
    def __init__(self, name, texture, pos):
        self.name = name
        self.texture = texture
        self.pos = pos

    def draw(self):
        screen.blit(self.texture, self.pos)


tioma = Character('Тёма', t_0, (100, 100))

