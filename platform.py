import pygame
import os

class Platform(pygame.sprite.Sprite):
    pygame.set_colorkey(0,0,0)

    def __init__(self, xy_start, platpic):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.xy = xy_start
        self.image = pygame.image.load(platpic)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = self.xy

