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
                        button.trigger()
                        break


class Button():
    """ contains implementation of buttons """

    def __init__(self, x: int, y: int, xsize: int, ysize: int, colour: Tuple[int, int, int], on_click: Callable, *args) -> None:
        self.rect = pygame.Rect(int(x-xsize/2), int(y-ysize/2), xsize, ysize)
        self.colour = colour
        self.on_click = on_click
        self.args = args

    def trigger(self) -> Any:
        return self.on_click(*self.args)

    def test_collision(self, x, y) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        else:
            return False

    def render(self, surface):
        dimmness = 0.5
        if self.test_collision(*pygame.mouse.get_pos()):
            colour = (self.colour[0]*dimmness, self.colour[1]*dimmness, self.colour[2]*dimmness)
        else:
            colour = self.colour
        pygame.draw.rect(surface, colour, self.rect)


class home_screen(menu):
    """ Contains the implementation of menu specific to the main menu """

    def alter_difficulty(self, do_increase: bool):
        if do_increase:
            if self.difficulty == self.difficulty.easy:
                self.difficulty = self.difficulty.medium
            elif self.difficulty == self.difficulty.medium:
                self.difficulty = self.difficulty.hard
        else:
            if self.difficulty == self.difficulty.hard:
                self.difficulty = self.difficulty.medium
            elif self.difficulty == self.difficulty.medium:
                self.difficulty = self.difficulty.easy
        self.difficulty = self.difficulty

    def __init__(self, game_instance) -> None:
        self.game_instance = game_instance
        self.difficulty = self.game_instance.difficulty_option.easy
        self.buttons = [

            Button(int(1920/2), int(1080/2 - 200),
                   120, 40, (0, 150, 0), self.game_instance.start_game, self.difficulty),

            Button(int(1920/2 - 250), int(1080/2),
                   120, 40, (0, 150, 0), self.alter_difficulty, False),
            Button(int(1920/2 + 250), int(1080/2),
                   120, 40, (0, 150, 0), self.alter_difficulty, True),

            Button(int(1920/2), int(1080/2 + 200),
                   120, 40, (150, 0, 0), self.game_instance.quit)

        ]
