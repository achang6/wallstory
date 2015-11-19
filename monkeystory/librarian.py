import pygame
from player import User                 
from filereader import readimagesfile   # returns a dictionary
from pygame.sprite import spritecollide
from wallcon import *
from platform import Platform

class Level():
    def __init__(self):
        super(Level,self).__init__()
        # set up image dictionary
        self.picbox = readimagesfile('imagekeys.txt')
        self.image = self.picbox['foggyforest']
        # get width and height from background image
        self.rect  = self.image.get_rect()
        # background image centered with screen
        self.rect.x = (WINW - self.rect.width) / 2
        self.rect.y = (WINH - self.rect.height) / 2
        self.xoriginal = self.rect.x
        self.yoriginal = self.rect.y
        # background velocity 
        self.dx = 0
        self.dy = 0
        # size of actual map
        # different from screen
        # may be smaller than image
        self.truew = 2560
        self.trueh = 1440
        # sprite lists
        self.platformlist = pygame.sprite.Group()
        self.spritelist = pygame.sprite.Group()
        # platform set up
        # x,y,w,h
        platformsprites = (
                self.topboundary = platform(0,-50,2560,50),
                self.leftboundary = platform(-50,-50,50,1540),
                self.rightboundary = platform(0,1440,2560,50),
                self.bottomboundary = platform(2560,0,50,1540)
                )
        for p in platformsprites:
            p.havesthour(self.truew,self.trueh)
            self.platformlist.add(p)
            self.spritelist.add(p)
        

    def levelshift(self,dx,dy):
        # speed of movement of world
        # preferably dx >>> dy
        self.dx = dx
        self.dy = dy

    def update(self):
        # adjust pseudo position
        self.rect.x += self.dx
        self.rect.y += self.dy

        # LR boundaries
        if self.rect.x > 0:
            self.rect.x = 0
        if self.rect.x < (WINW - self.rect.width):
            self.rect.x = WINW - self.rect.width
        # TB boundaries
        if self.rect.y > 0:
            self.rect.y = 0
        if self.rect.y < (WINH - self.rect.height):
            self.rect.y = WINH - self.rect.height

        # actually reposition
        self.rect.topleft = (self.rect.x,self.rect.y)


