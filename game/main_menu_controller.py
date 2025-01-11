from pygame.event import Event

from game.stories.base_story_controller import *
from media_data import *
from game.settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN)


class BaseMenu():
    def __init__(self, text: str, buttons_text: list[str]):
        self.title = font_1.render(text, True, (0, 0, 0))
        self.buttons_text = []
        self.button_width = 300
        self.buttons_height = 150
        self.space_between = 100
        self.space_bottom = 400
        self.selected = None
        self.button_rects = []
        for button_text in buttons_text:
            self.buttons_text.append(font_1.render(button_text, True, (255, 255, 255)))
            self.button_rects.append(pygame.Surface((self.button_width, self.buttons_height)))

    def calculate_coordinate(self):
        match len(self.buttons_text):
            case 1:
                return [(WIDTH // 2 - self.button_width // 2, HEIGHT // 2 - self.buttons_height // 2)]

            case 2:
                return [(WIDTH // 2 - self.button_width - self.space_between // 2,
                         HEIGHT // 2 - self.buttons_height - self.space_bottom),
                        (WIDTH // 2 + self.button_width + self.space_between // 2,
                         HEIGHT // 2 - self.buttons_height - self.space_bottom)]

    def draw_title(self):
        title_coordinate = (300, 100)

        screen.blit(self.title, title_coordinate)

    def draw_buttons(self):
        coordinates = self.calculate_coordinate()

        for i in range(len(self.buttons_text)):
            button_rect = self.button_rects[i]

            text_rect = self.buttons_text[i].get_rect(
                center=(
                    button_rect.get_width() // 2,
                    button_rect.get_height() // 2
                )
            )

            button_rect.blit(self.buttons_text[i], text_rect)
            screen.blit(button_rect, coordinates[i])

    def draw(self):
        self.draw_title()
        self.draw_buttons()


    def process_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button_rect in self.button_rects:
                if button_rect.collidepoint(event.pos):





class MainMenuStoryController(BaseStoryController):
    def __init__(self):
        super().__init__()
        pass

    def game(self):
        menu = BaseMenu('привет', ['привет', 'пока'])

        while not menu.selected:

            clock = pygame.time.Clock()

            screen.fill((255, 255, 255))

            menu.draw()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            clock.tick(FPS)
