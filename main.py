import pygame
from pygame import FULLSCREEN

from settings import *

from main_controller import MainController


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=FULLSCREEN)


main = MainController()
main.game_loop()




