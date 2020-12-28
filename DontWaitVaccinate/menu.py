class menu():
    """ Contains menu implementation and state """

    def __init__(self, game_instance):
        self.game_instance = game_instance
        self.buttons = []

    def render(self, surface):
        for button in self.buttons:
            button.render(surface)

    def process_event(self, event):
        pass


class home_screen(menu):
    """ Contains the implementation of menu specific to the main menu """

    def __init__(self, game_instance):
        super().__init__(game_instance)
        self.buttons = []


class button():
    """ contains implementation of buttons """
