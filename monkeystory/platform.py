import pygame
from wallcon import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, specs):
        super(Platform, self).__init__()
        # 0:x  1:y  2:w  3:h  4:c
        x = specs[0]
        y = specs[1]
        self.xy = (x,y)
        self.width  = specs[2]
        self.height = specs[3]
        self.image  = pygame.Surface(self.xy)
        self.image.fill(specs[4])

    def update(self):
        self.rect.topleft = self.xy
