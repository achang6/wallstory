import pygame
from wallcon import *
from pygame.sprite import spritecollide

class Player(pygame.sprite.Sprite):
    #### basic attribute declarations ####
    # track what direction player is facing
    direction = 'R'
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

    def gravity(self):
        # define gravity O.O
        if self.dy == 0:
            self.dy = 1
        elif self.dy > ymovespeed / 2:
            self.dy = ymovespeed / 2
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

    def crashcontingencyY(self):
        # vertical collision testing
        wallbox = spritecollide(self,self.level.platform_list,False)
        for wall in wallbox:
            # in the event that we bump into...
            if self.dy > 0 and self.rect.top < wall.rect.top:
                # if falling
                self.rect.bottom = wall.rect.top
                # stop goint through floors
                self.dy = 0
            elif self.dy < 0 and self.rect.bottom > wall.rect.bottom:
                # if rising
                self.rect.top = wall.rect.bottom
                # stop hanging from ceilings
                self.dy = 1
        if self.rect.bottom > WINH and self.dy > 0:
            self.rect.bottom = WINH
        if self.rect.top < 0 and self.dy < 0:
            self.rect.top = 0

    def crashcontingencyX(self):
        # horizontal collision testing
        wallbox = spritecollide(self,self.level.platform_list,False)
        for wall in wallbox:
            # in the event that we bump into something (wall)
            if self.dx > 0 and self.rect.left < wall.rect.left:
                # if moving right
                self.rect.right = wall.rect.left
            elif self.dx < 0 and self.rect.right > wall.rect.right:
                # if moving left
                self.rect.left = wall.rect.right
        if self.rect.right > WINW and self.dx > 0:
            self.rect.right = WINW
        if self.rect.left < 0 and self.dx < 0:
            self.rect.left = 0

    def useportal(self):
        # check for portals
        portalbox = spritecollide(self,self.level.portal_list,False)
        if portalbox != []:
            return portalbox[0].destination
        else:
            return 0
 
    def update(self):
        #### move ####
        # and so there was gravity
        self.gravity()

        
        # the second dimension (...jumping/falling)
        # aka vertical motion
        self.rect.y += self.dy
        
        # horizontal motion
        self.rect.x += self.dx

        # check collisions horizontally
        self.crashcontingencyX()
        
        # check collisions vertically
        self.crashcontingencyY()
 

        # face right, face left
        if self.direction == 'R':
            self.image = self.rightface[0]
        else:
            self.image = self.leftface[0]
    
           
          
'''# horizontal collisions
        self.rect.x += self.
        contact_walls = spritecollide(self, self.walls, False)
        for contact in contact_walls:
            if self. > 0:
                self.rect.right = contact.rect.left
            elif self. < 0: 
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
