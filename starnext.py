# import modules
import pygame
import os
import readfiles  # Readmapsfile, Readimagesfile
from wallconstants import *        # constants: FPS, WINW, WINH, TILEW, TILEH, TILEF, lowercase colors
import user
import platform



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
current_level   = 0
# initiate sprite groups
sprite_list     = pygame.sprite.Group()
platform_list   = pygame.sprite.Group()



# main function
def game_cycle():
    Playing = True
    lvl_tracker = 1

    # main loop ------------------------------------------------------------
    while Playing:
        # keep track of if level has changed
        lvl_tracker, migrate = level_changed(lvl_tracker, lvl)
        if migrate:
            lvl_width = levels[lvl]['width'] * TILEW
            lvl_height = levels[lvl]['height'] * TILEF
            lvl_object = levels[lvl]['map_object']
            plats_assemble(lvl)

            monkey_x = levels[lvl]['xy_state']['user'][0] * TILEW + WINW / 2 - lvl_width / 2 
            monkey_y = levels[lvl]['xy_state']['user'][1] * TILEF + WINH / 2 - lvl_height / 2
            mainmonkey = user.User(sprite_lib['horngirl'], monkey_x, monkey_y)
            mainmonkey.walls = platform_list
            sprite_list.add(mainmonkey)

        # event handling loop -----------------------------------------------
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
                '''if event.key == pygame.K_UP and event.key == pygame.K_RIGHT:
                    # direction = UPR
                    mainmonkey.accelerate(pixspeed, -pixspeed)
                if event.key == pygame.K_UP and event.key == pygame.K_LEFT:
                    # direction = UPL
                    mainmonkey.accelerate(-pixspeed, -pixspeed)
                if event.key == pygame.K_DOWN and event.key == pygame.K_RIGHT:
                    # direction = DOWNR
                    mainmonkey.accelerate(pixspeed, pixspeed)
                if event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
                    # direction = DOWNL
                    mainmonkey.accelerate(-pixspeed, pixspeed)'''
        # work space ------------------------------------------------------

        sprite_list.update()
        screen.fill(black)
        sprite_list.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    game_cycle()
