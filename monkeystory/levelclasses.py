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

    # background image
    background = None
    
    # misc properties
    truewidth = 1024
    trueheight = 720

    # world limits
    worldx = 0          # varies with level
    worldxshift = 0     # must be 0 at start of level
    xshiftmax = 0       # varies with level
    worldy = 0          # varies with level
    worldyshift = 0     # must be 0 at start of level
    yshiftmax = 0       # varies with level

    # allow player to reach edge of screen when background has
    xlimitbreak = False
    ylimitbreak = False

    # load image dictionary
    ilibrarian = readimagesfile('imagekeys.txt')

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        # horizontal boundaries
        # ....

        # update properties of all sprites
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        # refresh first
        screen.fill(BLACK)
        screen.blit(self.background, (self.worldx, self.worldy))
        # pygame.sprite.Group() draw function
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def worldrevolution(self, xshift, yshift):
        # change the world

        # if screen doesn't touch right edge of background
        if self.worldxshift > self.xshiftmax:
            # if screen doesn't touch left edge of background
            if self.worldxshift < -self.xshiftmax:
                # chain player
                self.xlimitbreak = False
                # track overall movement of world
                self.worldx += xshift
                self.worldxshift += xshift
                # move everything else
                for ledge in self.platform_list:
                    ledge.rect.x += xshift
                for enemy in self.enemy_list:
                    enemy.rect.x += xshift
        # if screen has reached L or R edge of background
        else:
            # release player
            self.xlimitbreak = True

        # if screen doesn't touch bottom of background    
        if self.worldyshift < self.yshiftmax:
            # if screen doesn't touch top of background
            if self.worldyshift > -self.yshiftmax:
                # chain player
                self.ylimitbreak = False
                # track vertical movement of world
                self.worldy += yshift
                self.worldyshift += yshift
                # move everything 
                for ledge in self.platform_list:
                    ledge.rect.y += yshift
                for enemy in self.enemy_list:
                    enemy.rect.y += yshift
        # if screen has reached T or B edge of background
        else:
            # release player
            self.ylimitbreak = True

# So the journey begins
class Level00(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['foggyforest']
        self.truewidth = 2560
        self.trueheight = 1709
        self.worldy = WINH - self.trueheight
        self.xshiftmax = WINW - self.truewidth
        self.yshiftmax = WINH - self.trueheight

        # platform creation array
        level = (
                platform.REDGRASS,
                platform.BLUEGRASS,
                platform.GREENGRASS,
                platform.BLACKGRASS
                )

        # plug level into platform_list
        for ledge in level:
            plat = platform.Platform(ledge)
            plat.player = self.player
            self.platform_list.add(plat)


