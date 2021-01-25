import pygame
import random

from . import spritesheet, world, entity

from . import vector

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

        self.npcs = [NPC(spritesheet1) for i in range(50)]

        # Initialise World
        self.world = world.World(d['size'], d['density'])

    def render(self, surface, font):
        """ Render every subobject of game state """
        self.world.render_ground(surface, font, self.cam_pos)
        self.player.render(surface, font, self.cam_pos)
        for npc in self.npcs:
            npc.render(surface, font, self.cam_pos)

    def process_event(self, event) -> None:
        """ Process an event """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player.m_up = True
            elif event.key == pygame.K_s:
                self.player.m_down = True
            elif event.key == pygame.K_a:
                self.player.m_left = True
            elif event.key == pygame.K_d:
                self.player.m_right = True
            elif event.key == pygame.K_LSHIFT:
                print("Sprinting")
                self.player.sprinting = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.player.m_up = False
            elif event.key == pygame.K_s:
                self.player.m_down = False
            elif event.key == pygame.K_a:
                self.player.m_left = False
            elif event.key == pygame.K_d:
                self.player.m_right = False
            elif event.key == pygame.K_LSHIFT:
                self.player.sprinting = False

    def update(self, delta) -> None:
        """ Update game state with time delta 'delta' """
        self.player.update(delta, self.npcs+[self.player])
        self.cam_pos = self.update_camera(0.2 * delta/16.0)
        for entity in self.npcs:
            entity.update(delta, self.npcs+[self.player])

    def update_camera(self, fraction):
        cam_pos = self.cam_pos
        player_pos = self.player.pos
        return cam_pos[0] + ((player_pos[0]-(640/2)) - cam_pos[0]) * fraction, \
            cam_pos[1] + ((player_pos[1]-(360/2)) - cam_pos[1]) * fraction


class NPC(entity.Entity):
    """ Contains the current state of an NPC """

    def __init__(self, spritesheet) -> None:
        super().__init__([random.randint(-500, 500), random.randint(-500, 500)],
                         spritesheet.get_images(random.randint(0, 3), random.randint(0, 1)))
        self.target = [0,0]
        self.sleep = random.randint(0, 2000)
        self.arrived = True
        
    def update(self, delta, entities):
        if self.arrived:
            self.sleep -= delta
            if self.sleep <= 0:
                self.arrived = False
                self.target = [random.randint(-500, 500), random.randint(-500,500)]
            
        else:
            if vector.length(vector.subtract(self.target, self.pos)) < 100:
                self.arrived = True
                self.sleep = random.randint(2000, 5000)
                self.m_dir = [0,0]
            else:
                self.m_dir = list(vector.normalise(vector.subtract(self.target, self.pos)))
        super().update(delta, entities)


class Player(entity.Entity):
    """ Contains the current state of the player """

    def __init__(self, sprites) -> None:
        self.m_up = False
        self.m_right = False
        self.m_down = False
        self.m_left = False
        super().__init__([0, 0], sprites)

    def update(self, delta, entities):
        diagonal_compensation = 0.7 if (self.m_up ^ self.m_down) and (self.m_left ^ self.m_right) else 1.0
        sprinting_compensation =  1.5 if self.sprinting else 1.0
        speed = diagonal_compensation * sprinting_compensation * 2
        if self.m_up ^ self.m_down:
            self.m_dir[1] = -speed if self.m_up else speed
        else:
            self.m_dir[1] = 0
        if self.m_right ^ self.m_left:
            self.m_dir[0] = speed if self.m_right else -speed
        else:
            self.m_dir[0] = 0
        super().update(delta, entities)
