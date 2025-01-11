from pygame import Surface

from game.media_data import small_font


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

    def draw(self, on: Surface):
        on.blit(self.rendered, self.text_rect)
