class game():
    def __init__(self):
        self.running = True
        self.game_state = False

class game_state():
    difficulty_options = {"easy":{}, "medium":{}, "hard":{}}
    def __init__(self, difficulty):
        self.player = Player(self.difficulty_options[difficulty]["player_health"])

class Player():
    def __init__(self, health):
        self.health = health
