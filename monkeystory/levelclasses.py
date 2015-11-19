import pygame
from player import User
from filereader import readimagesfile
from wallcon import *
from platform import Platform

class Level():
    #### declaration zone ######################################
    # sprite lists
    platform_list = None
    enemy_list = None

    # background image
    background = None
    
    # misc properties
    truewidth = 1280
    trueheight = 720

    # world limits
    worldxshift = 0
    xshiftmax = WINW - truewidth
    
    # load image dictionary
    ilibrarian = readimagesfile('imagekeys.txt')

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        
    def draw(self, screen):
        # refresh
        screen.fill(WHITE)
        screen.blit(self.background, (self.worldxshift // 3, 0))
        # pygame.sprite.Group() draw function
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def worldrevolution(self, xshift, yshift):
        # track overall movement of world
        self.worldxshift += xshift
        # move everything else
        for platform in self.platform_list:
            platform.rect.x += xshift
        for enemy in self.enemy_list:
            enemy.rect.x += xshift

class Level01(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['foggyforest']
        self.truewidth = 2560
        self.trueheight = 1440

        # platform creation array
        level = (
                plat1 = platform(1400,1280,200,10),
                plat2 = platform(1600,1180,200,10),
                plat3 = platform(1800,1080,200,10),
                plat4 = platform(2000, 980,200,10)
                )

        # plug level into platform_list
        for platform in level:
            self.platform_list.add(platform)

class Level02(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['foggyforest']
        self.truewidth = 2560
        self.trueheight = 1440

        # platform creation array
        level = (
                plat1 = platform(1400,1280,100,50),
                plat2 = platform(1200,1180,100,50),
                plat3 = platform(1000,1080,100,50),
                plat4 = platform(800 , 980,100,50),
                )

        # plug level into platform_list
        for platform in level:
            self.platform_list.add(platform)


