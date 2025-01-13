from pygame import Surface


class BaseScene:
    def __init__(self, screen: Surface):
        self.is_end = False
        self.screen = screen

    def game(self) -> 'BaseScene':
        raise NotImplementedError

