import pygame
import os
import math
from wallcon import *
from pygame.sprite import spritecollide

class User(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super(User, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = self.image.get_width()
        self.rect.h = self.image.get_height()
        self.dx = 0
        self.dy = 0
        self.walls = None
   
    def accelerate(self,x,y):
        self.dx = x
        self.dy = y

    def update(self):
        # horizontal collisions
        self.rect.x += self.dx
        contact_walls = spritecollide(self, self.walls, False)
        for contact in contact_walls:
            if self.dx > 0:
                self.rect.right = contact.rect.left
            elif self.dx < 0: 
                self.rect.left = contact.rect.right

        # vertical collisions
        self.rect.y += self.dy
        contact_walls = spritecollide(self, self.walls, False)
        for contact in contact_walls:
            if self.dy > 0:
                self.rect.bottom = contact.rect.top
            if self.dy < 0: 
                self.rect.top = contact.rect.bottom
        
        # horizontal limits
        if self.rect.x > WINW - 64 - self.rect.w:
            self.rect.x = WINW - 64 - self.rect.w
        if self.rect.x < 64:
            self.rect.x = 64
        
        # vertical limits
        if self.rect.y > WINH - 64 - self.rect.h:
            self.rect.y = WINH - 64 - self.rect.h
        if self.rect.y < 64:
            self.rect.y = 64


