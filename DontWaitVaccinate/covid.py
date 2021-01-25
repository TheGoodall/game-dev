from . import vector
import random, pygame

class emission():
    def __init__(self, pos, length):
        self.transparancy = 1
        self.pos = pos
        self.length = length

    def update(self, covids):
        # if self.transparancy == 1.0:
            
        self.transparancy -= 0.1

    def render(self, surface, font, cam_pos):
        pass
        

class covid():
    def __init__(self, parent, load=0):
        self.load = load
        self.parent = parent
        self.defence = 5
        self.damage = 0
        self.health = 100

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
        num_emits = self.emit_timer // 250
        self.emit_timer: int = self.emit_timer % 250
        num_coughs = self.cough_timer // 2000
        self.cough_timer = self.cough_timer % 2000

        for _ in range(num_emits):
            self.emissions.append(emission(self.parent.pos, 25))
        for _ in range(num_coughs):
            self.emissions.append(emission(self.parent.pos, 250))

        for iterated_emission in self.emissions:
            iterated_emission.update(covids)
    def render(self):
        pass
