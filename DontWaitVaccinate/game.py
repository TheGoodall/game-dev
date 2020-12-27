from enum import Enum
import pygame


class game():
    class difficulty_options(Enum):
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


class game_state():
    def __init__(self, difficulty):
        self.player = Player(difficulty["player_health"])


class Player():
    def __init__(self, health):
        self.health = health
