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
    truewidth = 1280
    trueheight = 720

    # world limits
    worldxshift = 0
    xshiftmax = 0

    # load image dictionary
    ilibrarian = readimagesfile('imagekeys.txt')

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        # horizontal boundaries

        # update properties of all sprites
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        # refresh first
        screen.fill(BLACK)
        screen.blit(self.background, (self.worldxshift, WINH-self.trueheight))
        # pygame.sprite.Group() draw function
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def worldrevolution(self, xshift, yshift):
        # track overall movement of world
        self.worldxshift += xshift
        # move everything else
        for ledge in self.platform_list:
            ledge.rect.x += xshift
        for enemy in self.enemy_list:
            enemy.rect.x += xshift

# So the journey begins
class Level00(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['foggyforest']
        self.truewidth = 2560
        self.trueheight = 1440
        self.xshiftmax = WINW - self.truewidth

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

# first step down the road
class Level01(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['foggyforest']
        self.truewidth = 2560
        self.trueheight = 1440
        self.xshiftmax = WINW - self.truewidth

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

# Another step down the road
class Level02(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['foggyforest']
        self.truewidth = 2560
        self.trueheight = 1440
        self.xshiftmax = WINW - self.truewidth

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

# Fork in the road
class Level03(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['foggyforest']
        self.truewidth = 2560
        self.trueheight = 1440
        self.xshiftmax = WINW - self.truewidth

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

# Journey into the Earth: Eternal Flames
class Level04(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['foggyforest']
        self.truewidth = 2560
        self.trueheight = 1440
        self.xshiftmax = WINW - self.truewidth

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

# Path to the End
class Level05(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['foggyforest']
        self.truewidth = 2560
        self.trueheight = 1440
        self.xshiftmax = WINW - self.truewidth

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

# Great Hall
class Level06(Level):
    def __init__(self,player):
        # sub class
        Level.__init__(self,player)

        # set background
        self.background = self.ilibrarian['foggyforest']
        self.truewidth = 2560
        self.trueheight = 1440
        self.xshiftmax = WINW - self.truewidth

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


