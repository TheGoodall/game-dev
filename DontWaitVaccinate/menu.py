class menu():
    """ Contains menu implementation and state """

    def __init__(self, game_instance) -> None:
        self.game_instance = game_instance
        self.buttons = []

    def render(self, surface) -> None:
        for button in self.buttons:
            button.render(surface)

    def process_event(self, event) -> None:
        pass


class home_screen(menu):
    """ Contains the implementation of menu specific to the main menu """

    def __init__(self, game_instance) -> None:
        super().__init__(game_instance)
        self.buttons = []


class button():
    """ contains implementation of buttons """
