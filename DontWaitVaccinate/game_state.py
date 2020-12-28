class game_state():
    """ Contains the current game state, including the player, the world, and any NPCs """
    # Initialise with difficulty options (d)

    def __init__(self, d) -> None:

        # Initialise Player
        self.player = Player(d["player_health"])

        # Initialise World
        self.world = World(d['size'], d['density'])


class Player():
    """ Contains the current state of the player """

    def __init__(self, health) -> None:
        self.health = health


class World():
    """ Contains the current state of the world, e.g. buildings """

    def __init__(self, size, density) -> None:
        pass
