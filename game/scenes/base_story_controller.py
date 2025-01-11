

class BaseSceneController:
    def __init__(self):
        self.is_end = False

    def game(self) -> 'BaseSceneController':
        raise NotImplementedError