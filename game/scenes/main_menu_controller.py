import pygame
from pygame import Surface
from pygame.event import Event

from game.media_data import big_font
from game.media_data import small_font
from game.settings import FPS
from game.settings import HEIGHT
from game.settings import WIDTH
from game.scenes.base_story_controller import BaseSceneController

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN)


class TextBox:
    def __init__(
            self,
            text,
            *,
            left_top: tuple[int, int] | None = None,
            center: tuple[int, int] | None = None
    ):
        self.text = text
        self.center = center
        try:
            self.rendered = small_font.render(text, True, (255, 255, 255))
            self.text_rect = self.__create_text_rect(left_top, center)
        except Exception as e:
            raise ValueError(f'Error on creating TextBox({text=})') from e

    def __create_text_rect(
            self,
            left_top: tuple[int, int] | None = None,
            center: tuple[int, int] | None = None
    ):
        if center is not None:
            return self.rendered.get_rect(
                center=center
            )
        elif left_top is not None:
            return self.rendered.get_rect(
                topleft=left_top
            )
        else:
            raise ValueError(f'Set left_top or center for TextBox')

    def draw(self, on: Surface = screen):
        on.blit(self.rendered, self.text_rect)


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

    def draw(self, on: Surface = screen):
        self.text_box.draw(self.surface)
        on.blit(self.surface, self.coords)


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
            button.draw()

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


class BlackSceneController(BaseSceneController):
    def __init__(self):
        super().__init__()

    def game(self) -> BaseSceneController | None:
        while True:
            clock = pygame.time.Clock()
            screen.fill((0, 0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            clock.tick(FPS)



