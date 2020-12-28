from typing import Any, Callable

import pygame


class menu():
    """ Contains menu implementation and state """

    buttons = []

    def render(self, surface) -> None:
        for button in self.buttons:
            button.render(surface)

    def process_event(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.test_collision(x, y):
                        button.trigger()
                        break


class home_screen(menu):
    """ Contains the implementation of menu specific to the main menu """

    def __init__(self, game_instance) -> None:
        self.game_instance = game_instance
        self.buttons = []


class Button():
    """ contains implementation of buttons """

    def __init__(self, x: int, y: int, xsize: int, ysize: int, on_click: Callable) -> None:
        self.rect = pygame.Rect(x, y, xsize, ysize)
        self.on_click = on_click

    def trigger(self) -> Any:
        return self.on_click()

    def test_collision(self, x, y) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        else:
            return False
