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
    level = None
    
    # class functions
    def __init__(self, image):
        super(Player, self).__init__()
        # set up image
        self.rightface.append(image)
        image = pygame.transform.flip(image,True,False)
        self.leftface.append(image)
        self.image = self.rightface[0]
        # set up rect obj and attributes
        self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y
        self.rect.w = self.image.get_width()
        self.rect.h = self.image.get_height()
        self.dx = 0
        self.dy = 0
        # jump law

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
        # call when 'jump' key pressed
        # first check if player is on a platform.
        self.rect.y += 2        
        harvest = spritecollide(self,self.level.platform_list,False)
        self.rect.y -= 2  
        # then 'jump' if not airborne
        if len(harvest) > 0 or self.rect.bottom >= WINH-self.rect.h:
            # jump
            self.dy = -10

    def leftmotion(self):
        # call when left movement key is held down
        self.dx = -xmovespeed
        self.direction = 'L'

    def rightmotion(self):
        # call when right movement key is held down
        self.dx = xmovespeed
        self.direction = 'R'

    def stop(self):
        # call when a movement key is released
        self.dx = 0

    def update(self):
        #### move ####
        # and so there was gravity
        self.gravity()

        # horizontal motion
        self.rect.x += self.dx
        if self.direction == 'R':
            self.image = self.rightface[0]
        else:
            self.image = self.leftface[0]
            
        # horizontal collision testing
        wallbox = spritecollide(self,self.level.platform_list,False)
        for wall in wallbox:
            # in the event that we bump into something (wall)
            if self.dx > 0: 
                # if moving right
                self.rect.right = wall.rect.left
            elif self.dx < 0:
                # if moving left
                self.rect.left = wall.rect.right

        # the second dimension (...jumping/falling)
        self.rect.y += self.dy
        
        # vertical collision testing
        wallbox = spritecollide(self,self.level.platform_list,False)
        for wall in wallbox:
            # in the event that we bump into...
            if self.dy > 0:
                # if falling
                self.rect.bottom = wall.rect.top
            elif self.dy < 0:
                # if rising
                self.rect.top = wall.rect.bottom

        '''# horizontal collisions
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
        '''
