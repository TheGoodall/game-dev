import random, pygame

from pygame.math import Vector2 as V

class emission():
    def __init__(self, pos, distance):
        self.speed = 25
        self.pos = pos
        self.direction = V()
        self.direction.from_polar((1, random.random()*360))
        self.distance = distance
        self.length = V(0,0)
        self.shorten = 0

    def infect(self, covids):
        pass
        # for covid in covids:
            # if ((self.pos) - covid.parent.pos).magnitude() < 15:
                # covid.load += random.randint(1, 1000)
        # return self
    def update(self):
        self.pos += self.direction * self.speed

    def render(self, surface, font, cam_pos):
        pygame.draw.line(surface, (38,93,200), self.pos-cam_pos, (self.pos+(self.direction*self.speed))-cam_pos)
        

class covid():
    def __init__(self, parent, load=0):
        self.load = load
        self.parent = parent
        self.defence = random.randint(1, 50)
        self.damage = 0
        self.health = random.randint(100, 1000)


        self.emit_timer: int = 0
        self.cough_timer: int = 0
        
        self.emissions = []
        
    def update(self, delta, covids):
        self.damage += self.load * (delta/16)
        self.load = self.load - self.defence * (delta/16) if self.damage > 0 else 0
        if self.damage > 100:
            self.emit_timer += delta
        if self.damage > 1000:
            self.cough_timer += delta
        self.emission_delay = random.randint(15, 50)
        self.cough_delay = random.randint(150, 500)
        num_emits = self.emit_timer // 250
        self.emit_timer: int = self.emit_timer % 250
        num_coughs = self.cough_timer // 2000
        self.cough_timer = self.cough_timer % 2000

        for _ in range(num_emits):
            self.emissions.append(emission(self.parent.pos, 25))
        for _ in range(num_coughs):
            self.emissions.append(emission(self.parent.pos, 250))
        for iemission in self.emissions:
            if iemission.length == V(0,0):
                self.emissions.remove(iemission)

    def render(self, surface, font, cam_pos):
        for emission in self.emissions:
            emission.render(surface, font, cam_pos)
