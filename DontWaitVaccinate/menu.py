from typing import Any, Callable, Tuple

import pygame


class menu():
    """ Contains menu implementation and state """

    buttons = []
    texts = []

    def render(self, surface, font, bg=True) -> None:
        """ Render each subobject of the menu """
        if bg:
            surface.fill((35, 35, 35))
        for button in self.buttons:
            button.render(surface, font)
        for text in self.texts:
            text.render(surface, font)

    def process_event(self, event) -> None:
        """ Process events relating to the menu """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = event.pos
                for button in self.buttons:
                    if button.test_collision(pos[0], pos[1]):
                        button.trigger()
                        break


class Button():
    """ contains implementation of buttons """

    def __init__(self, x: int, y: int, xsize: int, ysize: int, colour: Tuple[int, int, int], text: str, on_click: Callable, *args) -> None:
        self.rect = pygame.Rect(int(x-xsize/2), int(y-ysize/2), xsize, ysize)
        self.colour = colour
        self.text = text
        self.rendered_text = None
        self.on_click = on_click
        self.args = args

    def trigger(self) -> Any:
        """ Run the function assigned to the button """
        return self.on_click(*self.args)

    def test_collision(self, x, y) -> bool:
        """ Test if a single point is within the button """
        if self.rect.collidepoint(x, y):
            return True
        else:
            return False

    def render(self, surface, font):
        """ Render the button, darker if overlapping with mouse """
        dimmness = 0.5
        if self.test_collision(*pygame.mouse.get_pos()):
            colour = (self.colour[0]*dimmness, self.colour[1]
                      * dimmness, self.colour[2]*dimmness)
        else:
            colour = self.colour
        pygame.draw.rect(surface, colour, self.rect)
        if not self.rendered_text:
            self.rendered_text = font.render(self.text, True, (0, 0, 0))
        surface.blit(self.rendered_text, self.rect)


class Text():
    """ Object for rendering text """
    def __init__(self, text: str, x: int, y: int) -> None:
        self.text = text
        self.rect = pygame.Rect(x, y, 100, 100)
        self.rendered_text = None

    def render(self, surface, font) -> None:
        if not self.rendered_text:
            self.rendered_text = font.render(self.text, True, (255, 255, 255))
        surface.blit(self.rendered_text, self.rect)

    def change_text(self, newtext: str) -> None:
        self.text = newtext
        self.rendered_text = None


# Difficulty options possible
difficulty_option = {
    "easy":     {"difficulty": "First Wave", "r": 1},
    "medium":   {"difficulty": "Second Wave", "r": 3},
    "hard":     {"difficulty": "The U.K. Variant", "r": 15}
}


class Difficulty_display(Text):
    """ Child class of Text which displays the current difficulty """
    def __init__(self, x, y):
        self.currentDifficulty = None
        super().__init__("Difficulty: ", x, y)

    def render(self, surface, font, difficulty) -> None:
        if difficulty_option[difficulty]['difficulty'] != self.currentDifficulty:
            self.currentDifficulty = difficulty_option[difficulty]['difficulty']
            self.change_text("Difficulty: {}".format(
                self.currentDifficulty))
        super().render(surface, font)

class pause_screen(menu):
    """ Contains the implementation of menu specific to the main menu """

    def __init__(self, game_instance, won=False) -> None:
        self.game_instance = game_instance
        self.buttons = [

            Button(int(640/2), int(480/2 + 50),
                   120, 40, (0, 150, 0), "Quit to Menu", self.game_instance.quit_to_menu),
            Button(int(640/2), int(480/2 + 100),
                   120, 40, (150, 0, 0), "Quit!", self.game_instance.quit)

        ]
        if not won:
            self.buttons.append(Button(int(640/2), int(480/2),
                120, 40, (0, 150, 0), "Resume", (self.game_instance.unpause)))
        self.texts = [
            Text("Don't Wait! Vaccinate!", 250, 45),
            Text("Paused", 270, 100)
        ] if not won else  [
            Text("Don't Wait! Vaccinate!", 250, 45),
            Text("You Won! Covid has been eradicated!", 230, 100)
        ]

    def render(self, surface, font) -> None:
        """ Render the pause menu """
        super().render(surface, font, False)

class home_screen(menu):
    """ Contains the implementation of menu specific to the main menu """

    def alter_difficulty(self, do_increase: bool) -> None:
        """ Change the current difficulty either one up or one down, but remains within bounds """
        if do_increase:
            if self.difficulty == "easy":
                self.difficulty = "medium"
            elif self.difficulty == "medium":
                self.difficulty = "hard"
        else:
            if self.difficulty == "hard":
                self.difficulty = "medium"
            elif self.difficulty == "medium":
                self.difficulty = "easy"

    def __init__(self, game_instance) -> None:
        self.game_instance = game_instance
        self.difficulty = "easy"
        self.buttons = [

            Button(int(640/2), int(480/2 - 100),
                   120, 40, (0, 150, 0), "Start", self.game_instance.start_game),

            Button(int(640/2 - 200), int(480/2),
                   60, 20, (0, 150, 0), "Easier", self.alter_difficulty, False),
            Button(int(640/2 + 200), int(480/2),
                   60, 20, (0, 150, 0), "Harder", self.alter_difficulty, True),

            Button(int(640/2), int(480/2 + 100),
                   60, 20, (150, 0, 0), "Quit!", self.game_instance.quit)

        ]
        self.texts = [
            Text("Don't Wait! Vaccinate!", 260, 50)
        ]
        self.difficulty_display = Difficulty_display(270, 240)

    def render(self, surface, font) -> None:
        """ Render the main menu """
        super().render(surface, font)
        self.difficulty_display.render(surface, font, self.difficulty)
