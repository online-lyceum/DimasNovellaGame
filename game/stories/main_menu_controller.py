import pygame
from pygame.event import Event
from pygame.examples.moveit import WIDTH

from game.settings import FPS
from game.settings import HEIGHT
from game.stories.base_story_controller import BaseStoryController
from game.media_data import big_font
from game.media_data import small_font

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN)


class Button:
    def __init__(
            self,
            text: str,
            coords: tuple[int, int],
            width=200,
            height=100
    ):
        self.text = text
        self.width = width
        self.height = height
        self.coords = coords
        self.rect = pygame.Rect(*coords, width, height)
        self.surface = pygame.Surface((width, height))
        self.rendered_text = small_font.render(text, True, (255, 255, 255))
        self.text_rect = self.rendered_text.get_rect(
            center=(
                self.surface.get_width() // 2,
                self.surface.get_height() // 2
            )
        )

    def draw(self):
        self.surface.blit(self.rendered_text, self.text_rect)
        screen.blit(self.surface, self.coords)


class BaseMenu:
    def __init__(self, title: str, buttons_text: list[str]):
        self.title = title
        self.rendered_title = big_font.render(self.title, True, (0, 0, 0))
        self.space_between = 100
        self.space_bottom = 400
        self.button_width = 200
        self.button_height = 100
        self.selected = None
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
                     HEIGHT // 2 - self.button_height - self.space_bottom),
                    (WIDTH // 2 + self.button_width + self.space_between // 2,
                     HEIGHT // 2 - self.button_height - self.space_bottom)]

    def draw_title(self):
        screen.blit(self.rendered_title, self.calculate_title_coordinate())

    def draw_buttons(self):
        for button in self.buttons:
            button.draw()

    def draw(self):
        self.draw_title()
        self.draw_buttons()

    def process_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    self.selected = button.text
                    return


class MainMenuStoryController(BaseStoryController):
    def __init__(self):
        super().__init__()

    def game(self) -> BaseStoryController | None:
        menu = BaseMenu('привет', ['привет'])

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
        return MainMenuStoryController()
