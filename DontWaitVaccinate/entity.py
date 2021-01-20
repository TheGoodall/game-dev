import math


class PhysicalObject():
    def __init__(self, pos):
        self.pos = pos

    def render(self, surface, font, cam_pos, sprite):
        """ Render object """
        pos = (self.pos[0]-cam_pos[0], self.pos[1]-cam_pos[1])
        surface.blit(sprite, pos)


def vec_subtract(vec1, vec2):
    return map(lambda x: x[0]-x[1], zip(vec1, vec2))


def vec_add(vec1, vec2):
    return map(lambda x: x[0]+x[1], zip(vec1, vec2))


def vec_length(vec):
    return math.sqrt(sum(map(lambda x: x**2, vec)))


def vec_normalise(vec):
    mag = vec_length(vec)
    if mag != 0:
        return map(lambda x: x/mag, vec)
    else:
        return map(lambda _: 0, vec)


def vec_scale(vec, scale):
    return map(lambda x: x*scale, vec)


class Entity(PhysicalObject):
    def __init__(self, pos, sprites):
        self.sprites = sprites
        self.sprite_state = 0
        self.sprite_dir = 1
        self.sprite_timer = 0
        self.sprinting = False
        self.m_up = False
        self.m_down = False
        self.m_left = False
        self.m_right = False
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
        speed_modifier = 1.5 if self.sprinting else 1.0
        if self.m_down and not self.m_up:
            if self.m_left ^ self.m_right:
                self.pos[1] += 3.5 * (delta/16.0) * speed_modifier
            else:
                self.pos[1] += 5 * (delta/16.0) * speed_modifier
                self.sprite_dir = 2
        elif self.m_up and not self.m_down:
            if self.m_left ^ self.m_right:
                self.pos[1] -= 3.5 * (delta/16.0) * speed_modifier
            else:
                self.pos[1] -= 5 * (delta/16.0) * speed_modifier
                self.sprite_dir = 0
        if self.m_left and not self.m_right:
            if self.m_up ^ self.m_down:
                self.pos[0] -= 3.5 * (delta/16.0) * speed_modifier
            else:
                self.pos[0] -= 5 * (delta/16.0) * speed_modifier
                self.sprite_dir = 3
        elif self.m_right and not self.m_left:
            if self.m_up ^ self.m_down:
                self.pos[0] += 3.5 * (delta/16.0) * speed_modifier
            else:
                self.pos[0] += 5 * (delta/16.0) * speed_modifier
                self.sprite_dir = 1
        if (self.m_up ^ self.m_down) or (self.m_left ^ self.m_right):
            self.sprite_timer -= delta
            if self.sprite_timer <= 0:
                self.sprite_state = (self.sprite_state + 1) % 4
                self.sprite_timer += 60 if self.sprinting else 100
        else:
            self.sprite_state = 1

        for entity in entities:
            if abs(self.pos[0] - entity.pos[0]) < 50 and abs(self.pos[1] - entity.pos[1]) < 30:
                difference = list(vec_subtract(self.pos, entity.pos))
                distance = vec_length(difference)
                if distance < 30:
                    direction = vec_normalise(difference)
                    force = list(vec_scale(direction, 30-distance))
                    self.pos = list(vec_add(self.pos, force))
                    entity.pos = list(vec_subtract(entity.pos, force))
