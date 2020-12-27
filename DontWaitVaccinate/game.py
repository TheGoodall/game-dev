from enum import Enum


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


class game_state():
    def __init__(self, difficulty):
        self.player = Player(difficulty["player_health"])


class Player():
    def __init__(self, health):
        self.health = health
