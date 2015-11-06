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
        self.image.fill(BLACK) 

    def update(self):
        self.rect.topleft = (self.rect.x,self.rect.y)
