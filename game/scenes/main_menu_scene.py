import pygame
from pygame.event import Event

from game.media_data import big_font
from game.scenes.base_scene import BaseSceneController
from game.scenes.black_scene import BlackSceneController
from game.settings import FPS
from game.settings import HEIGHT
from game.settings import WIDTH
from game.UI.button import Button

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN)


class BaseMenu:
    def __init__(self, title: str, buttons_text: list[str]):
        self.title = title
        self.rendered_title = big_font.render(self.title, True, (0, 0, 0))
        self.space_between = 100
        self.space_bottom = 100
        self.button_width = 200
        self.button_height = 100
        self.selected = ''
        self.buttons = []
        coords = self.calculate_buttons_coordinates(len(buttons_text))
        for i, button_text in enumerate(buttons_text):
            self.buttons.append(
                Button(
                    button_text,
                    coords[i],
                    self.button_width,
                    self.button_height
                )
            )

    @staticmethod
    def calculate_title_coordinate() -> tuple[int, int]:
        return 300, 100

    def calculate_buttons_coordinates(self, button_count: int):
        match button_count:
            case 1:
                return [(WIDTH // 2 - self.button_width // 2,
                         HEIGHT // 2 - self.button_height // 2)]

            case 2:
                return [
                    (WIDTH // 2 - self.button_width - self.space_between // 2,
                     HEIGHT - self.button_height - self.space_bottom),
                    (WIDTH // 2 + self.button_width + self.space_between // 2,
                     HEIGHT - self.button_height - self.space_bottom)]

    def draw_title(self):
        screen.blit(self.rendered_title, self.calculate_title_coordinate())

    def draw_buttons(self):
        for button in self.buttons:
            button.draw(screen)

    def draw(self):
        self.draw_title()
        self.draw_buttons()

    def process_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    self.selected = button.text_box.text
                    return

    def draw_scene(self):
        if self.selected == '':
            return MainMenuSceneController()
        if self.selected == 'играть':
            return BlackSceneController()
        if self.selected == 'пока':
            return pygame.quit()


class MainMenuSceneController(BaseSceneController):
    def __init__(self):
        super().__init__()

    def game(self) -> BaseSceneController | None:
        menu = BaseMenu('привет', ['играть', 'пока'])

        while not menu.selected:
            clock = pygame.time.Clock()
            screen.fill((255, 255, 255))
            menu.draw()
            pygame.display.update()

            for event in pygame.event.get():
                menu.process_event(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            clock.tick(FPS)
        return menu.draw_scene()
