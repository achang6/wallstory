import pygame, os

class Monkeymain(self, image = pygame.image.load('images/princess.png'), x = 0, y = 0, speedmax = 2):
    def __init__(self):
        self.image = image
        self.posx = x
        self.posy = y
        self.dx = 0
        self.dy = 0
        self.maxspeed = speedmax
    # move user, hopefully collision check run before this is called
    def proceed(self, heading, speed):
        # modify direction of displacement
        if heading == 'UP':
            self.dy = -1
            self.dx = 0
        elif heading == 'down':
            self.dy = 1
            self.dx = 0
        elif heading == 'left':
            self.dy = 0
            self.dx = -1
        elif heading == 'right':
            self.dy = 0
            self.dx = 1
        elif heading == 'upright':
            self.dy = -1
            self.dx = 1
        elif heading == 'upleft':
            self.dy = -1
            self.dx = -1
        elif heading == 'downright':
            self.dy = 1
            self.dx = 1
        elif heading == 'downleft':
            self.dy = 1
            self.dx = -1
        # modify magnitude of displacement
        if self.dx <= self.maxspeed and self.dx >= self.maxspeed *= -1:
            self.dx *= speed
        else:
            self.dx = self.maxspeed
        if self.dy <= self.maxspeed and self.dy >= self.maxspeed *= -1:
            self.dy *= speed
        else:
            self.dy = self.maxspeed
        # displacement
        self.posx += self.dx
        self.posy += self.dy
