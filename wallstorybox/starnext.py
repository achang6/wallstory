# import modules
import pygame
import os
import user
import platform
import readfiles  # Readmapsfile, Readimagesfile
from wallconstants import *        # constants: FPS, WINW, WINH, TILEW, TILEH, TILEF, lowercase colors
from starfun import *



# Setup zone #######################################################
# mandatory: set up pygame
pygame.init()
# set up screen
pygame.display.set_caption('Wallstory 0')
screen          = pygame.display.set_mode((WINW, WINH))
background      = pygame.Surface(screen.get_size()).convert()
# set up clock
clock           = pygame.time.Clock()
playtime        = 0.0
# set up font
font            = pygame.font.SysFont('mono', 12, bold = True)
# track current level
current_lvl     = 0
# set up image dictionary
sprite_lib = readfiles.Readimagesfile('starnext_images.txt')
#initiate sprite groups
sprite_list     = pygame.sprite.Group()
platform_list   = pygame.sprite.Group()



# main function
def game_cycle():
    Playing = True
    lvl_tracker = 1

    # main loop ------------------------------------------------------
    while Playing:

        # keep track of if level has changed
        lvl_tracker, migrate = lvl_changed(lvl_tracker, current_lvl)
        if migrate:
            # reset sprite groups for new level
            platform_list.empty()
            sprite_list.empty()
            # change platforms





            plat_xy = plats_assemble(current_lvl)
            plat = platform.Platform(plat_xy, sprite_lib['corner'])
            platform_list.add(plat) 
            sprite_list.add(plat)

            monk_x, monk_y = activate_monkey(current_lvl)
            mainmonkey = user.User(sprite_lib['horngirl'], \
                    monk_x, monk_y)
            mainmonkey.walls = platform_list
            sprite_list.add(mainmonkey)

        # event handling loop ----------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Playing = False             # exit
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    mainmonkey.accelerate(0,  pixspeed)
                if event.key == pygame.K_DOWN:
                    mainmonkey.accelerate(0, -pixspeed)
                if event.key == pygame.K_LEFT:
                    mainmonkey.accelerate( pixspeed, 0)
                if event.key == pygame.K_RIGHT:
                    mainmonkey.accelerate(-pixspeed, 0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    Playing = False         # exit
                if event.key == pygame.K_UP:
                    # direction = UP
                    mainmonkey.accelerate(0, -pixspeed)
                if event.key == pygame.K_DOWN:
                    # direction = DOWN
                    mainmonkey.accelerate(0,  pixspeed)
                if event.key == pygame.K_LEFT:
                    # direction = LEFT
                    mainmonkey.accelerate(-pixspeed, 0)
                if event.key == pygame.K_RIGHT:
                    # direction = RIGHT
                    mainmonkey.accelerate( pixspeed, 0)
                '''if event.key == pygame.K_UP \
                        and event.key == pygame.K_RIGHT:
                    # direction = UPR
                    mainmonkey.accelerate(pixspeed, -pixspeed)
                if event.key == pygame.K_UP \
                        and event.key == pygame.K_LEFT:
                    # direction = UPL
                    mainmonkey.accelerate(-pixspeed, -pixspeed)
                if event.key == pygame.K_DOWN \
                        and event.key == pygame.K_RIGHT:
                    # direction = DOWNR
                    mainmonkey.accelerate(pixspeed, pixspeed)
                if event.key == pygame.K_DOWN \
                        and event.key == pygame.K_LEFT:
                    # direction = DOWNL
                    mainmonkey.accelerate(-pixspeed, pixspeed)'''
        # work space ---------------------------------------------

        sprite_list.update()
        screen.fill(blue)
        sprite_list.draw(screen)
        pygame.display.update()

if __name__ == '__main__':
    game_cycle()
