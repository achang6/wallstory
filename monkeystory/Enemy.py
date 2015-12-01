import pygame
from wallcon import *
from pygame.sprite import spritecollide
from filereader import readimagesfile

class Baddy(pygame.sprite.Sprite):
    #### basic attribute declarations ####
    # track direction baddy is facing
    direction = 'R'
    rightface = []
    leftface = []
    # track distance to player
    x2prey = 0
    y2prey = 0
    # some baddies are faster than others (horizontal)
    baddyspeed = 1
    # some baddies... can fly!
    wings = False
    # running out of image dictionary names
    iselfies = readimagesfile('imagekeys.txt')
    
    #### class functions ####
    def __init__(self,player):
        super(Player,self).__init__()
        # set up image
        image = self.iselfies['Batbaddy']
        self.rightface.append(image)
        image = pygame.transform.flip(image,True,False)
        self.leftface.append(image)
        self.image = self.rightface[0]
        # set up rect obj and attributes
        self.rect = self.image.get_rect()
        self.rect.w = self.image.get_width()
        self.rect.h = self.image.get_height()
        # find your prey
        self.player = player

    def update(self):
        x2prey = self.rect.x - self.player.rect.x
        y2prey = self.rect.y - self.player.rect.y

        # in the presence of player
        if abs(x2prey) < 300:
            if abs(y2prey) < 200:
                # to the left to the left
                if x2prey < 0:
                    self.direction = 'L'
                    self.image = self.leftface[0]
                    if abs(x2prey) > 10:
                        self.rect.x -= baddyspeed
                # to the right to the right
                elif x2prey > 0:
                    self.direction = 'R'
                    self.image = self.rightface[0]
                    if abs(x2prey) > 10:
                        self.rect.x += baddyspeed
                # I can fly
                if self.wings == True:
                    # in place
                    if abs(y2prey) < 1:
                        self.rect.y = self.player.rect.y
                    # up in the sky
                    elif y2prey < 0:
                        self.rect.y -= 1
                    # burrowing with wings
                    elif y2prey > 0:
                        self.rect.y += 1

#### subclasses ####

class Batbaddy(Baddy):
    def __init__(self,player):
        Baddy.__init__(self,player)

