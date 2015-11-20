import pygame
from wallcon import *
from pygame.sprite import spritecollide

class Player(pygame.sprite.Sprite):
    #### basic attribute declarations ####
    # track what direction player is facing
    direction = 'r'
    rightface = []
    leftface = []
    # track player velocities
    dx = 0
    dy = 0
    # track solid objects
    obstructions = None
    
    # class functions
    def __init__(self, image, x, y):
        super(Player, self).__init__()
        # set up image
        self.rightface.append(image)
        image = pygame.transform.flip(image,True,False)
        self.leftface.append(image)
        self.image = self.rightface[0]
        # set up rect obj and attributes
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = self.image.get_width()
        self.rect.h = self.image.get_height()
        self.dx = 0
        self.dy = 0

    def gravity(self):
        # define gravity O.O
        if self.dy == 0:
            self.dy = 1
        else:
            self.dy += 0.35
        # As Atlas carries the Earth, so does the Earth carry you
        if self.rect.y >= (WINH - self.rect.h) and self.dy >= 0:
            self.dy = 0
            self.rect.y = WINH - self.rect.h

    def jump(self):
        #### classic action ####
        # call when 'jump' key pressed
        self.rect.y += 2
        contactharvest = spritecollide(self,self.level.platform_list,False)
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


