import pygame
from wallcon import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, specs = []):
        super(Platform, self).__init__()
        # 0:x  1:y  2:w  3:h  4:c
        self.wh = (specs[2],specs[3])
        self.image  = pygame.Surface(self.wh)
        self.rect = self.image.get_rect()
        self.rect.x = specs[0]
        self.rect.y = specs[1]
        self.dx = 0
        self.dy = 0
        self.image.fill(BLACK) 
        self.truewidth = 0
        self.trueheight = 0
        self.truexpos = 0
        self.trueypos = 0
        self.xoriginal = self.rect.x
        self.yoriginal = self.rect.y
    
    def worldrevolution(self, dx, dy):
        self.dx = -dx
        self.dy = -dy 
    
    # must be called immediately after each instance
    def harvesthour(self, mapwidth, mapheight):
        self.truewidth = mapwidth
        self.trueheight = mapheight
        # accounts for difference in positions of each platform
        self.truexpos = self.truewidth - self.rect.x
        self.trueypos = self.trueheight - self.rect.y

    def update(self):
        # adjust position
        self.rect.x += self.dx
        self.rect.y += self.dy

        # deny screen from surpassing map boundaries
        # left and right boundaries
        if self.rect.x > self.xoriginal:
            self.rect.x = self.xoriginal
        elif self.rect.x < (self.xoriginal + WINW - self.truewidth):
            self.rect.x = self.xoriginal + WINW - self.truewidth
        # top and bottom boundaries
        if self.rect.y > self.yoriginal: 
            self.rect.y = self.yoriginal
        elif self.rect.y < (self.yoriginal + WINH - self.trueheight):
            self.rect.y = self.yoriginal + WINH - self.trueheight

        # position platforms accordingly
        self.rect.topleft = (self.rect.x,self.rect.y)
