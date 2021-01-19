import pygame

from . import spritesheet


class game_state():
    """ Contains the current game state, including the player, the world, and any NPCs """
    # Initialise with difficulty options (d)

    def __init__(self, d) -> None:

        self.cam_pos = (-1920/2, -1080/2)

        spritesheet1 = spritesheet.spritesheet(
            "DontWaitVaccinate/images/spritesheet.png")
        spritesheet2 = spritesheet.spritesheet(
            "DontWaitVaccinate/images/spritesheet 2.png")

        # Initialise Player
        self.player = Player(spritesheet1.get_images(0, 0))

        # Initialise World
        self.world = World(d['size'], d['density'])

    def render(self, surface, font):
        """ Render every subobject of game state """
        self.world.render_ground(surface, font, self.cam_pos)
        self.player.render(surface, font, self.cam_pos)

    def process_event(self, event) -> None:
        """ Process an event """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player.m_up = True
            if event.key == pygame.K_s:
                self.player.m_down = True
            if event.key == pygame.K_a:
                self.player.m_left = True
            if event.key == pygame.K_d:
                self.player.m_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.player.m_up = False
            if event.key == pygame.K_s:
                self.player.m_down = False
            if event.key == pygame.K_a:
                self.player.m_left = False
            if event.key == pygame.K_d:
                self.player.m_right = False

    def update(self, delta) -> None:
        """ Update game state with time delta 'delta' """
        self.player.update(delta)
        self.cam_pos = self.update_camera(0.2 * delta/16.0)
        pass

    def update_camera(self, fraction):
        cam_pos = self.cam_pos
        player_pos = self.player.pos
        return cam_pos[0] + ((player_pos[0]-(1920/2)) - cam_pos[0]) * fraction, \
               cam_pos[1] + ((player_pos[1]-(1080/2)) - cam_pos[1]) * fraction


class PhysicalObject():
    def __init__(self, pos):
        self.pos = pos

    def render(self, surface, font, cam_pos, sprite):
        """ Render object """
        pos = (self.pos[0]-cam_pos[0], self.pos[1]-cam_pos[1])
        surface.blit(sprite, pos)


class Entity(PhysicalObject):
    def __init__(self, pos, sprites):
        self.sprites = sprites
        self.sprite_state = 0
        self.sprite_dir = 1
        self.sprite_timer = 0
        self.m_up = False
        self.m_down = False
        self.m_left = False
        self.m_right = False
        super().__init__(pos)

    def render(self, surface, font, cam_pos):
        sprites = self.sprites[self.sprite_dir]
        if self.sprite_state == 3:
            sprite = sprites[1]
        else:
            sprite = sprites[self.sprite_state]

        super().render(surface, font, cam_pos, sprite)

    def update(self, delta):
        if self.m_down and not self.m_up:
            if self.m_left ^ self.m_right:
                self.pos[1] += 3.5 * (delta/16.0)
            else:
                self.pos[1] += 5 * (delta/16.0)
                self.sprite_dir = 2
        elif self.m_up and not self.m_down:
            if self.m_left ^ self.m_right:
                self.pos[1] -= 3.5 * (delta/16.0)
            else:
                self.pos[1] -= 5 * (delta/16.0)
                self.sprite_dir = 0
        if self.m_left and not self.m_right:
            if self.m_up ^ self.m_down:
                self.pos[0] -= 3.5 * (delta/16.0)
            else:
                self.pos[0] -= 5 * (delta/16.0)
                self.sprite_dir = 3
        elif self.m_right and not self.m_left:
            if self.m_up ^ self.m_down:
                self.pos[0] += 3.5 * (delta/16.0)
            else:
                self.pos[0] += 5 * (delta/16.0)
                self.sprite_dir = 1
        if (self.m_up ^ self.m_down) or (self.m_left ^ self.m_right):
            self.sprite_timer -= delta
            if self.sprite_timer <= 0:
                self.sprite_state = (self.sprite_state + 1) % 4
                self.sprite_timer += 100
        else:
            self.sprite_state = 1
        


class NPC(Entity):
    pass


class Player(Entity):
    """ Contains the current state of the player """

    def __init__(self, sprites) -> None:
        super().__init__([0, 0], sprites)


class World():
    """ Contains the current state of the world, e.g. buildings """

    def __init__(self, size: int, density: int) -> None:
        self.ground_texture = pygame.image.load(
            "DontWaitVaccinate/images/grass.jpg")
        self.ground_texture = pygame.transform.scale(
            self.ground_texture, (500, 500))

    def render_ground(self, surface, font, cam_pos):
        screen_size = surface.get_size()
        texture_size = self.ground_texture.get_size()
        cam_pos = round(cam_pos[0]), round(cam_pos[1])

        render_offset = -(cam_pos[0] % texture_size[0]
                          ), -(cam_pos[1] % texture_size[1])

        count = round(screen_size[0] / texture_size[0] +
                      1), round(screen_size[0] / texture_size[0] + 1)

        render = []

        for i in range(count[0]):
            for j in range(count[1]):
                render_pos = (
                    render_offset[0] + i * texture_size[0],
                    render_offset[1] + j * texture_size[1]
                )
                render.append((self.ground_texture, render_pos))

        surface.blits(render)
