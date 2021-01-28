import random, pygame

from pygame.math import Vector2 as V

import copy

class emission():
    def __init__(self, parent, pos, distance, r, direction = None, colour = (38,93,200), speed=1):
        self.colour = colour
        self.r = r
        self.parent = parent
        self.speed = speed
        self.pos = pos
        self.direction = V()
        self.collided = False
        
        if not direction:
            self.direction.from_polar((1, random.random()*360)) 
        else:
            self.direction = direction.normalize()

        self.distance = distance
        self.length = V(0,0)
        self.age = 0.0

    def collide(self, covids):
        pass

    def update(self, covids, delta):
        self.pos += (self.direction * self.speed) * (delta/16)
        self.length = self.speed * delta/16 * self.age
        self.age += self.speed * (delta/16) / self.distance
        self.collide(covids)

    def render(self, surface, font, cam_pos):
        pygame.draw.line(surface, self.colour, self.pos+(self.direction * self.speed  * self.age)-cam_pos, (self.pos+(self.direction*self.speed))-cam_pos,2)
        
class covid_particle(emission):
    def collide(self, covids):
        for covid in covids:
            if covid != self.parent:
                if (self.pos - covid.parent.pos).magnitude() < self.r:
                    print(self.r)
                    covid.load += 100

class vaccine(emission):
    def collide(self, covids):
        for covid in covids:
            if covid != self.parent:
                if ((self.pos) - covid.parent.pos).magnitude() < 15:
                    self.collided = True
                    covid.load -= 1000

class covid():
    def __init__(self, parent, r, load=0):
        self.r = r
        self.load = load
        self.parent = parent
        self.defence = 1/10
        self.damage = 0


        self.emit_timer: int = 0
        self.cough_timer: int = 0
        
        self.emissions = []
        
    def update(self, delta, covids):

        self.damage += self.load * (delta/16)
        self.load = self.load - self.defence * (delta/16) if self.damage > 0 else 0

        if self.damage > 100:
            self.emit_timer += delta * self.load / 100
        if self.damage > 10000:
            self.cough_timer += delta

        self.emission_delay = random.randint(15, 50)
        self.cough_delay = random.randint(1500, 5000)

        if self.emit_timer > self.emission_delay:
            self.emit_timer: int = self.emit_timer % self.emission_delay
            self.emissions.append(covid_particle(self, copy.copy(self.parent.pos), max(self.load/30, 25), self.r))

        if self.cough_timer > self.cough_delay:
            self.cough_timer: int = self.cough_timer % self.cough_delay
            for _ in range(10):
                self.emissions.append(covid_particle(self, copy.copy(self.parent.pos),150, self.r))

        for iemission in self.emissions:
            iemission.update(covids, delta)
            if iemission.length > 1.0:
                self.emissions.remove(iemission)

    def render(self, surface, font, cam_pos):
        for emission in self.emissions:
            emission.render(surface, font, cam_pos)
