import pygame

from DontWaitVaccinate.game_state import game_state

from DontWaitVaccinate.menu import home_screen


class game():
    """ Contains the state of the game as a whole, including menu screens. """

    # Possible difficulty options

    def __init__(self) -> None:
        self.running = True
        self.game_state = False
        self.paused = None
        self.menu = home_screen(self)

    def start_game(self, difficulty) -> None:
        self.game_state = game_state(difficulty)
        self.menu = None

    def quit(self) -> None:
        self.running = False

    def render(self, surface, font) -> None:
        if self.menu:
            self.menu.render(surface, font)
        elif self.game_state:
            self.game_state.render(surface, font)
            if self.paused:
                self.paused.render(surface, font)

    def loop(self) -> None:
        self.events()

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.menu:
                self.menu.process_event(event)
