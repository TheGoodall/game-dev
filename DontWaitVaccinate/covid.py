import random, pygame

from pygame.math import Vector2 as V

import copy

class emission():
    def __init__(self, parent, pos, distance):
        self.parent = parent
        self.speed = 1
        self.pos = pos
        self.direction = V()
        self.direction.from_polar((1, random.random()*360))
        self.distance = distance
        self.length = V(0,0)
        self.age = 0.0

    def infect(self, covids):
        for covid in covids:
            if covid != self.parent:
                if ((self.pos) - covid.parent.pos).magnitude() < 15:
                    covid.load += random.randint(1000, 10000000)
        # return self
    def update(self, covids):
        self.pos += self.direction * self.speed
        self.length = self.speed * self.age
        self.age += self.speed / self.distance
        self.infect(covids)

    def render(self, surface, font, cam_pos):
        pygame.draw.line(surface, (38,93,200), self.pos+(self.direction * self.speed  * self.age)-cam_pos, (self.pos+(self.direction*self.speed))-cam_pos,5)
        

class covid():
    def __init__(self, parent, load=0):
        self.load = load
        self.parent = parent
        self.defence = random.randint(1, 4)
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
        self.cough_delay = random.randint(1500, 5000)
        num_emits = self.emit_timer // self.emission_delay
        self.emit_timer: int = self.emit_timer % self.emission_delay
        num_coughs = self.cough_timer // self.cough_delay
        self.cough_timer = self.cough_timer % self.cough_delay

        for _ in range(num_emits):
            self.emissions.append(emission(self, copy.copy(self.parent.pos), 25))
        for _ in range(num_coughs):
            for _ in range(10):
                self.emissions.append(emission(self, copy.copy(self.parent.pos), 250))
        for iemission in self.emissions:
            iemission.update(covids)
            if iemission.length > 1.0:
                self.emissions.remove(iemission)

    def render(self, surface, font, cam_pos):
        for emission in self.emissions:
            emission.render(surface, font, cam_pos)
