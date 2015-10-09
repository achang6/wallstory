# import modules
import pygame
import os
import readfiles  # Readmapsfile, Readimagesfile
from wallconstants import *        # constants: FPS, WINW, WINH, TILEW, TILEH, TILEF, lowercase colors


pygame.init()                                                           # initiate pygame
pygame.display.set_caption('Wallstory 0')                               # set window caption
screen = pygame.display.set_mode((WINW, WINH))                          # set window surface object
background = pygame.Surface(screen.get_size()).convert()                # set background surface, convert for blitting
background.fill(green)                                                  # OPTIONAL: color the background
sprite_dictionary = readfiles.Readimagesfile('starnext_images.txt')     # set image dictionary
levels = readfiles.Readmapsfile('starPusherLevels.txt')                 # set levels array/dictionary
clock = pygame.time.Clock()                                             # set pygame clock
playtime = 0.0                                                          # OPTIONAL: container for time app active
font = pygame.font.SysFont('mono', 12, bold = True)                     # set font
levelnum = 0                                                            # track index of current level

sprite_list     = pygame.sprite.Group()
platform_list   = pygame.sprite.Group()



def game_cycle():
    Playing = True
    
    for x in range(levels[levelnum]['width']):
        for y in range(levels[levelnum]['height']):
            if levels[levelnum]['map_object'][x][y] == '#':
                platform = Platform(sprite_dictionary['corner'],levels[levelnum]['map_object'][x],levels[levelnum]['map_object'][x][y])
                platform_list.add(platform)

    # main loop ------------------------------------------------------------
    while Playing:
        needredraw = False
        # even handling loop -----------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Playing = False             # exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    Playing = False         # exit
                if event.key == pygame.K_UP:
                    direction = UP
                if event.key == pygame.K_DOWN:
                    direction = DOWN
                if event.key == pygame.K_LEFT:
                    direction = LEFT
                if event.key == pygame.K_RIGHT:
                    direction = RIGHT
                if event.key == pygame.K_UP and event.key == pygame.K_RIGHT:
                    direction = UPR
                if event.key == pygame.K_UP and event.key == pygame.K_LEFT:
                    direction = UPL
                if event.key == pygame.K_DOWN and event.key == pygame.K_RIGHT:
                    direction = DOWNR
                if event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
                    direction = DOWNL
        # work space ------------------------------------------------------

        pygame.display.update()
        self.screen.blit(self.background, (0,0))

   





if __name__ == '__main__':
    HelloWorld().run()
