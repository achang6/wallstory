import pygame
import platform
from player import Player
from filereader import readimagesfile
from wallcon import *

class Level():
    #### declaration zone ######################################
    # sprite lists
    platform_list = None
    enemy_list = None
    portal_list = None

    # background image
    background = None
    
    # misc properties
    truewidth = 1024
    trueheight = 720
    xplaypos = 0
    yplaypos = 0

    # world limits
    worldx = 0        
    xshiftmax = 0
    worldy = 0      
    yshiftmax = 0

    # allow player to reach edge of screen when background has
    llimit = False
    rlimit = False
    tlimit = False
    blimit = False

    # load image dictionary
    ilibrarian = readimagesfile('imagekeys.txt')

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.portal_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        # horizontal boundaries
        # ....

        # update properties of all sprites
        self.platform_list.update()
        self.enemy_list.update()
        self.portal_list.update()

    def draw(self, screen):
        # refresh first
        screen.fill(BLACK)
        screen.blit(self.background, (self.worldx, self.worldy))
        # pygame.sprite.Group() draw function
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.portal_list.draw(screen)

    def worldrevolution(self, xshift, yshift):
        # change the world

        # if screen doesn't touch R edge of background
        if self.worldx > self.xshiftmax:
            # chain player
            self.rlimit = False
            # track overall movement of world
            self.worldx += xshift
            # move everything else
            for ledge in self.platform_list:
                ledge.rect.x += xshift
            for enemy in self.enemy_list:
                enemy.rect.x += xshift
            for portal in self.portal_list:
                portal.rect.x += xshift
        # if screen has reached L or R edge of background
        else:
            # release player
            self.rlimit = True

        # if screen doesn't touch L edge of background
        if self.worldx < 0:
            # chain player
            self.llimit = False
            # track overall movement of world
            self.worldx += xshift
            # move everything else
            for ledge in self.platform_list:
                ledge.rect.x += xshift
            for enemy in self.enemy_list:
                enemy.rect.x += xshift
            for portal in self.portal_list:
                portal.rect.x += xshift
        # if screen has reached L or R edge of background
        else:
            # release player
            self.llimit = True

        # if screen doesn't touch B of background    
        if self.worldy > self.yshiftmax:
            # chain player
            self.blimit = False
            # track vertical movement of world
            self.worldy += yshift
            # move everything 
            for ledge in self.platform_list:
                ledge.rect.y += yshift
            for enemy in self.enemy_list:
                enemy.rect.y += yshift
            for portal in self.portal_list:
                portal.rect.y += yshift
        # if screen has reached T or B edge of background
        else:
            # release player
            self.blimit = True

        # if screen doesn't touch T of background    
        if self.worldy < 0:
            # chain player
            self.tlimit = False
            # track vertical movement of world
            self.worldy += yshift
            # move everything 
            for ledge in self.platform_list:
                ledge.rect.y += yshift
            for enemy in self.enemy_list:
                enemy.rect.y += yshift
            for portal in self.portal_list:
                portal.rect.y += yshift
        # if screen has reached T or B edge of background
        else:
            # release player
            self.tlimit = True

    def wheretostart(self,worldxnow,worldynow):
        # assigns starting position of background
        # set background x position
        self.worldx = worldxnow
        self.xshiftmax = WINW - self.truewidth
        # set background  Y position
        self.worldy = worldynow
        self.yshiftmax = WINH - self.trueheight
 

# So the journey begins
class Level01(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['stage001']
        self.truewidth = 1528
        self.trueheight = 720
        self.wheretostart(0,WINH - self.trueheight)

        # player ?
        self.xplaypos = HWINW
        self.yplaypos = HWINH

        # platform creation array
        level = (
                (0,580,1600,50,None),
                (320,0,50,720,None)
                )

        # plug level into platform_list
        for ledge in level:
            plat = platform.Platform(ledge)
            plat.player = self.player
            plat.image.set_colorkey(BLACK)
            self.platform_list.add(plat)

        # door to next level    
        tostage02 = platform.Platform((1350,530,50,50,PORTAL))
        tostage02.player = self.player
        tostage02.destination = 2
        self.portal_list.add(tostage02)
        
# So the journey begins
class Level02(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['stage002']
        self.truewidth = 1024
        self.trueheight = 4560
        self.wheretostart(0,0)
        
        # player?
        self.xplaypos = 450
        self.yplaypos = 200
       
        # platform creation array
        level = (
                (0,500,600,50,None),
                (350,0,50,500,None),
                (600,700,200,50,SWAMP),
                (400,850,200,50,SWAMP),
                (200,1000,200,50,SWAMP),
                (500,1150,150,50,SWAMP),
                (200,1300,150,50,SWAMP),
                (400,1450,150,50,SWAMP),
                (600,1600,150,50,SWAMP),
                (800,1750,50,50,SWAMP),
                (600,1900,150,50,SWAMP),
                (400,2050,150,50,SWAMP),
                (600,2200,200,50,SWAMP),
                (300,2350,300,50,SWAMP),
                (500,2500,300,50,SWAMP),
                (200,2650,300,50,SWAMP),
                (500,2800,200,50,SWAMP),
                (750,2950,150,50,SWAMP),
                (600,3100,100,50,SWAMP),
                (400,3250,50,50,SWAMP),
                (200,3400,150,50,SWAMP),
                (500,3550,250,50,SWAMP),
                (800,3700,400,50,SWAMP),
                (400,3850,350,50,SWAMP),
                (0,3900,401,50,SWAMP),
                (750,3900,50,50,SWAMP),
                (700,4050,400,50,SWAMP),
                (450,4200,350,50,SWAMP),
                (0,4350,350,50,SWAMP),
                (300,4500,450,50,SWAMP)
                )

        # plug level into platform_list
        for ledge in level:
            plat = platform.Platform(ledge)
            plat.player = self.player
            plat.image.set_colorkey(BLACK)
            self.platform_list.add(plat)

        # door to next level    
        tostage01 = platform.Platform((850,4510,50,50,PORTAL))
        tostage01.player = self.player
        tostage01.destination = 1
        self.portal_list.add(tostage01)
        



