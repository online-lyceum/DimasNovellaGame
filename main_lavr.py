class Scene:
    def __init__(self, *args, **kwargs):
        pass

    def draw(self):
        pass

class Hero:
    def __init__(self, *args, **kwargs):
        pass

class Menu:
    def __init__(self, *args, **kwargs):
        self.selected = None

    def draw(self):
        pass

class BaseStoryController:
    def __init(self):
        self._load_resources()
        self.is_end = False

    def _load_resources(self):
        pass

    def game(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass


class BathroomStoryController(BaseStoryController):
    def __init__(self):
        super().__init__(self)
        self.scenes = {}
        self.heroes = {}

    def game(self):
        self.scenes['mountes'].draw()
        menu = Menu('In what bathroom do you want to go?', 'Male', 'Female', is_fullscreen=True)
        while not menu.selected:
            self.scenes['mountes'].draw()
            menu.draw()
            menu.update()
        if menu.selected == 'Male':
            return MaleBathroomStoryController()
        if menu.selected == 'Female':
            return FemaleBathroomStoryController()

    def load_resources_for_first_mission(self):
        self.scenes['mountes'] = Scene('mountes.png', ...)
        self.heroes['John'] = Hero('Jong.png', ...)


class GameController:
    def __init__(self):
        pass

    def main_loop(self):
        active_story = BathroomStoryController()
        while not active_story.is_end:
            active_story = active_story.game()
