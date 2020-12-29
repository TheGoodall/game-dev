from typing import Any, Callable, Tuple

import pygame


class menu():
    """ Contains menu implementation and state """

    buttons = []

    def render(self, surface) -> None:
        for button in self.buttons:
            button.render(surface)

    def process_event(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = event.pos
                for button in self.buttons:
                    if button.test_collision(pos[0], pos[1]):
                        print("triggered")
                        button.trigger()
                        break


class Button():
    """ contains implementation of buttons """

    def __init__(self, x: int, y: int, xsize: int, ysize: int, colour: Tuple[int, int, int], on_click: Callable, *args) -> None:
        self.rect = pygame.Rect(x, y, xsize, ysize)
        self.colour = colour
        self.on_click = on_click
        self.args = args

    def trigger(self) -> Any:
        return self.on_click(self.args)

    def test_collision(self, x, y) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        else:
            return False

    def render(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)


class home_screen(menu):
    """ Contains the implementation of menu specific to the main menu """

    def __init__(self, game_instance) -> None:
        self.game_instance = game_instance
        self.difficulty = self.game_instance.difficulty_option.easy
        self.buttons = [
            Button(int(1920/2 - 30), int(1080/2 - 200),
                   60, 20, (0, 150, 0), self.game_instance.start_game, self.difficulty)
        ]
