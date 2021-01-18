import pygame

from DontWaitVaccinate.game_state import game_state

from DontWaitVaccinate.menu import home_screen
from DontWaitVaccinate.menu import pause_screen


class game():
    """ Contains the state of the game as a whole, including menu screens. """

    def __init__(self) -> None:
        self.running = True
        self.game_state = None
        self.paused = None
        self.menu = home_screen(self)

    def unpause(self) -> None:
        self.paused = None

    def quit_to_menu(self) -> None:
        self.game_state = None
        self.paused = None
        self.menu = home_screen(self)

    def start_game(self, difficulty) -> None:
        """ Start a new game and close the menu """
        self.game_state = game_state(difficulty)
        self.menu = None

    def quit(self) -> None:
        self.running = False

    def render(self, surface, font) -> None:
        """ Calls render on all subobjects of the game object """
        if self.menu:
            self.menu.render(surface, font)
        elif self.game_state:
            self.game_state.render(surface, font)
            if self.paused:
                self.paused.render(surface, font)

    def loop(self, delta) -> None:
        """ Run the game loop once """
        self.events()
        if not self.menu and self.game_state and not self.paused:
            self.game_state.update(delta)

    def events(self) -> None:
        """ Iterate through each event processing it """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.menu:
                self.menu.process_event(event)
            elif self.game_state:
                if self.paused:
                    self.paused.process_event(event)
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.paused = pause_screen(self)
                    self.game_state.process_event(event)
