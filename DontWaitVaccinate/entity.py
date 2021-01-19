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
        
