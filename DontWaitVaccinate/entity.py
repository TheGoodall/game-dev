import math
from . import vector, covid

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
        self.sprinting = False
        self.m_dir = [0,0]

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

    def update(self, delta, entities):
        self.covid.update(delta, map(lambda x: x.covid, entities))
        self.pos[0] += (delta/16) * self.m_dir[0]
        self.pos[1] += (delta/16) * self.m_dir[1]
        
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
            if abs(self.pos[0] - entity.pos[0]) < 50 and abs(self.pos[1] - entity.pos[1]) < 30:
                difference = list(vector.subtract(self.pos, entity.pos))
                distance = vector.length(difference)
                if distance < 30:
                    direction = vector.normalise(difference)
                    force = list(vector.scale(direction, 30-distance))
                    self.pos = list(vector.add(self.pos, force))
                    entity.pos = list(vector.subtract(entity.pos, force))
