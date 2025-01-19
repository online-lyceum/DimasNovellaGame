import pygame
from pygame import Surface
from pygame.event import Event

from game.media_data import big_font
from game.settings import HEIGHT
from game.settings import WIDTH
from game.UI.button import Button


class Menu:
    def __init__(self, title: str, buttons_text: list[str]):
        self.title = title
        self.rendered_title = big_font.render(self.title, True, (0, 0, 0))
        self.space_between = 200
        self.space_bottom= 600
        self.button_width = 300
        self.button_height = 100
        self.selected = ''
        self.buttons: list[Button] = []
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
                return [
                    (WIDTH // 2 - self.button_width // 2,
                     HEIGHT // 2 - self.button_height // 2)
                ]

            case 2:
                return [
                    (WIDTH // 2 - self.button_width - self.space_between // 2,
                     HEIGHT - self.button_height - self.space_bottom),
                    (WIDTH // 2 + self.space_between // 2,
                     HEIGHT - self.button_height - self.space_bottom)
                ]

            case 3:
                return [
                    (WIDTH // 2 - self.button_width - self.space_between // 2,
                     HEIGHT - self.button_height - self.space_bottom),
                    (WIDTH // 2 + self.space_between // 2,
                     HEIGHT - self.button_height - self.space_bottom),
                    (WIDTH // 2 - self.button_width // 2,
                     HEIGHT // 2)
                ]

            case 4:
                return [
                    (WIDTH // 2 - self.button_width - self.space_between // 2,
                     HEIGHT - self.button_height - self.space_bottom),
                    (WIDTH // 2 + self.space_between // 2,
                     HEIGHT - self.button_height - self.space_bottom),
                    (WIDTH // 2 - self.button_width - self.space_between // 2,
                     HEIGHT // 2),
                    (WIDTH // 2 + self.space_between // 2,
                     HEIGHT // 2)
                ]

    def draw_title(self, on: Surface):
        on.blit(self.rendered_title, self.calculate_title_coordinate())

    def draw_buttons(self, on: Surface):
        for button in self.buttons:
            button.draw(on)

    def draw(self, on: Surface):
        self.draw_title(on)
        self.draw_buttons(on)

    def process_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    self.selected = button.text_box.text
                    return
