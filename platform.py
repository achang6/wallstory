import pygame
import os

class Platform(pygame.sprite.Sprite):
    def __init__(self, xy_start, platpic):
        super(Platform, self).__init__()
        self.xy = xy_start
        self.image = platpic 
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
    def update(self):
        self.rect.center = self.xy

