

class BaseStoryController:
    def __init__(self):
        self.is_end = False

    def game(self) -> 'BaseStoryController':
        raise NotImplementedError