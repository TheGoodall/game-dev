from enum import Enum
import pygame

from DontWaitVaccinate.game_state import game_state

from DontWaitVaccinate.menu import home_screen


class game():
    """ Contains the state of the game as a whole, including menu screens. """

    # Possible difficulty options
    class difficulty_option(Enum):
        easy = {},
        medium = {},
        hard = {}

    def __init__(self) -> None:
        self.running = True
        self.game_state = False
        self.paused = False
        self.menu = home_screen(self)

    def start_game(self, difficulty) -> None:
        self.game_state = game_state(difficulty)

    def render(self, surface) -> None:
        if self.menu:
            self.menu.render(surface)

    def loop(self) -> None:
        self.events()

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
