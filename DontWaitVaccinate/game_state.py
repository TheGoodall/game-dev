import pygame


class game_state():
    """ Contains the current game state, including the player, the world, and any NPCs """
    # Initialise with difficulty options (d)

    def __init__(self, d) -> None:

        # Initialise Player
        self.player = Player(d['player_health'])

        # Initialise World
        self.world = World(d['size'], d['density'])

    def render(self, surface, font):
        self.world.render(surface, font)
        self.player.render(surface, font)


class Player():
    """ Contains the current state of the player """

    def __init__(self, health) -> None:
        self.health = health

    def render(self, surface, font):
        pass


class World():
    """ Contains the current state of the world, e.g. buildings """

    def __init__(self, size, density) -> None:
        pass

    def render(self, surface, font):
        pass
