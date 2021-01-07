import pygame


class game_state():
    """ Contains the current game state, including the player, the world, and any NPCs """
    # Initialise with difficulty options (d)

    def __init__(self, d) -> None:

        self.cam_pos = (0, 0)

        # Initialise Player
        self.player = Player()

        # Initialise World
        self.world = World(d['size'], d['density'])

    def render(self, surface, font):
        """ Render every subobject of game state """
        self.world.render(surface, font, self.cam_pos)
        self.player.render(surface, font, self.cam_pos)

    def process_event(self, event) -> None:
        """ Process an event """
        pass

    def update(self, delta) -> None:
        """ Update game state with time delta 'delta' """
        self.update_camera(0.5)
        pass

    def update_camera(self, fraction):
        cam_pos = self.cam_pos
        player_pos = self.player.pos

        return cam_pos[0] + (cam_pos[0] - player_pos[0]) * fraction, cam_pos[1] + (cam_pos[1] - player_pos[1]) * fraction




class PhysicalObject():
    def __init__(self, pos):
        self.pos = pos
    def render(self, surface, font, cam_pos):
        """ Render Entity """
        pass


class Entity(PhysicalObject):
    def __init__(self, pos):
        super().__init__(pos)


class NPC(Entity):
    pass


class Player(Entity):
    """ Contains the current state of the player """

    def __init__(self) -> None:
        super().__init__((0,0))


class World():
    """ Contains the current state of the world, e.g. buildings """

    def __init__(self, size: int, density: int) -> None:
        self.ground_texture = pygame.image.load(
            "DontWaitVaccinate/images/grass.jpg")
        self.ground_texture = pygame.transform.scale(
            self.ground_texture, (500, 500))

    def render(self, surface, font, cam_pos):
        """ Render world """
        self.render_ground(surface, font, cam_pos)

    def render_ground(self, surface, font, cam_pos):
        screen_size = surface.get_size()
        texture_size = self.ground_texture.get_size()
        cam_pos = round(cam_pos[0]), round(cam_pos[1])

        render_offset = -(cam_pos[0] % texture_size[0]
                          ), -(cam_pos[1] % texture_size[1])

        print(screen_size, texture_size)

        count = round(screen_size[0] / texture_size[0] +
                      1), round(screen_size[0] / texture_size[0] + 1)
        print(count)

        render = []

        for i in range(count[0]):
            for j in range(count[1]):
                render_pos = (
                    render_offset[0] + i * texture_size[0],
                    render_offset[1] + j * texture_size[1]
                )
                render.append((self.ground_texture, render_pos))

        surface.blits(render)
