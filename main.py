import pygame
from pygame import FULLSCREEN

from game.settings import *

from game.main_controller import MainController


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=FULLSCREEN)


main = MainController()
main.game_loop()




