from . import vector
import random, pygame

class covid():
    def __init__(self):
        self.load = 0
        self.defence = 5
        self.damage = 0
        self.health = 100

        self.emit_timer = 0
        self.cough_timer = 0
        
        self.emissions = []
        
    def update(self, delta):
        self.damage += self.load * (delta/16)
        self.load = self.load - self.defence * (delta/16) if self.damage > 0 else 0
        if damage > 100:
            self.emit_timer += delta
        if damage > 1000:
            self.cough_timer += delta
        num_emits = self.emit_timer / 250
        self.emit_timer = self.emit_timer % 250
        num_coughs = self.cough_timer / 2000
        self.cough_timer = self.cough_timer % 2000

    def update_emmisions(self, covids):
        for emission in self.emissions:
            emission.update(covids)
    def render(self):

    

class emission():
    def __init__(self, length):

        
