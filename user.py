import pygame
import os
import math

class User(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super(User, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_shift = 0
        self.y_shift = 0
        self.walls = None
    
    def accelerate(self, x, y):
        self.x_shift = x
        self.y_shift = y
    
    def update(self):
        if self.x_shift < 0:
            self.x_shift = math.ceil(self.x_shift * .99)
        elif self.x_shift > 0:
            self.x_shift = math.floor(self.x_shift * .99)
        if self.y_shift < 0:
            self.y_shift = math.ceil(self.y_shift * .99)
        elif self.y_shift > 0:
            self.y_shift = math.floor(self.y_shift * .99)


        # horizontal
        self.rect.x += self.x_shift
        contact_walls = pygame.sprite.spritecollide(self, self.walls, False)
        for contact in contact_walls:
            if self.x_shift > 0:
                self.rect.right = contact.rect.left
            elif self.x_shift < 0:
                self.rect.left = contact.rect.right
        
        # vertical
        self.rect.y += self.y_shift
        contact_walls = pygame.sprite.spritecollide(self, self.walls, False)
        for contact in contact_walls:
            if self.y_shift > 0:
                self.rect.bottom = contact.rect.top
            elif self.y_shift < 0:
                self.rect.top = contact.rect.bottom
