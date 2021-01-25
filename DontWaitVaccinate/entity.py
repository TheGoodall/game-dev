import math
from pygame.math import Vector2 as V
from . import covid

class PhysicalObject():
    def __init__(self, pos):
        self.pos = pos

    def render(self, surface, font, cam_pos, sprite):
        """ Render object """
        pos = self.pos - cam_pos
        surface.blit(sprite, pos-V(24,24))


class Entity(PhysicalObject):
    def __init__(self, pos, sprites):
        self.sprites = sprites
        self.sprite_state = 0
        self.sprite_dir = 1
        self.sprite_timer = 0
        self.sprinting = False
        self.m_dir = V(0,0)

        self.covid = covid.covid(self, 1000)
        super().__init__(pos)

    def render(self, surface, font, cam_pos):
        if self.pos[0] >= cam_pos[0] - 50 and \
                self.pos[0] <= cam_pos[0] + 1920 and \
                self.pos[1] >= cam_pos[1] - 50 and \
                self.pos[1] <= cam_pos[1] + 1080:
            sprites = self.sprites[self.sprite_dir]
            if self.sprite_state == 3:
                sprite = sprites[1]
            else:
                sprite = sprites[self.sprite_state]

            super().render(surface, font, cam_pos, sprite)
            self.covid.render(surface, font, cam_pos)

    def update(self, delta, entities):
        self.covid.update(delta, map(lambda x: x.covid, entities))
        self.pos += self.m_dir * (delta/16)
        
        if self.m_dir[1] < -abs(self.m_dir[0]):
            self.sprite_dir = 0
        elif self.m_dir[0] > abs(self.m_dir[1]):
            self.sprite_dir = 1
        elif self.m_dir[1] > abs(self.m_dir[0]):
            self.sprite_dir = 2
        elif self.m_dir[0] < -abs(self.m_dir[1]):
            self.sprite_dir = 3

        if self.m_dir[0] or self.m_dir[1]:
            self.sprite_timer -= delta
            if self.sprite_timer <= 0:
                self.sprite_state = (self.sprite_state + 1) % 4
                self.sprite_timer += 60 if self.sprinting else 100
        else:
            self.sprite_state = 1

        for entity in entities:
            if self == entity:
                continue
            distance = self.pos.distance_to(entity.pos)
            if distance < 30:
                correction = (self.pos - entity.pos).normalize() * ((30-distance) * 0.08)
                entity.pos -= correction
                self.pos += correction
