from enum import Enum
import pygame

from DontWaitVaccinate import game_state

class game():
    """ Contains the state of the game as a whole, including menu screens. """

    # Possible difficulty options
    class difficulty_option(Enum):
        easy = {},
        medium = {},
        hard = {}

    def __init__(self):
        self.running = True
        self.game_state = False
        self.paused = False

    def start(self, difficulty):
        self.game_state = game_state(difficulty)

    def render(self, surface):
        pass

    def loop(self):
        self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
