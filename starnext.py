# import modules
import pygame
import os
import readfiles  # Readmapsfile, Readimagesfile
from wallconstants import *        # constants: FPS, WINW, WINH, TILEW, TILEH, TILEF, lowercase colors
import user
import platform


pygame.init()                                                           # initiate pygame
pygame.display.set_caption('Wallstory 0')                               # set window caption
screen = pygame.display.set_mode((WINW, WINH))                          # set window surface object
background = pygame.Surface(screen.get_size()).convert()                # set background surface, convert for blitting
background.fill(gray)                                                   # OPTIONAL: color the background
spriteground = pygame.Surface(screen.get_size()).convert()              # set surface for sprites to blit onto screen after background
sprite_lib = readfiles.Readimagesfile('starnext_images.txt')            # set image dictionary
levels = readfiles.Readmapsfile('starPusherLevels.txt')                 # set levels array/dictionary
clock = pygame.time.Clock()                                             # set pygame clock
playtime = 0.0                                                          # OPTIONAL: container for time app active
font = pygame.font.SysFont('mono', 12, bold = True)                     # set font
lvl = 0                                                                 # track index of current level
sprite_list     = pygame.sprite.Group()
platform_list   = pygame.sprite.Group()



# Function zone ##################################################################################################

def plats_assemble(level_index):
    lvl = level_index
    lvl_width = levels[lvl]['width']
    lvl_height = levels[lvl]['height']

    platform_list.empty()
    sprite_list.empty()
    
    for x in range(lvl_width):
        for y in range(lvl_height):
            if levels[lvl]['map_object'][x][y] == '#':
                plat_x = TILEW * x
                plat_y = TILEF * y
                lvlw = TILEW * lvl_width
                lvlh = TILEF * lvl_height

                plats = platform.Platform((plat_x + WINW / 2 - lvlw / 2, plat_y + WINH / 2 - lvlh / 2), sprite_lib['corner'])
                
                platform_list.add(plats)
                sprite_list.add(plats)
    
def level_changed(before, after):
    old_lvl = before
    new_lvl = after
    if old_lvl == new_lvl:
        return old_lvl, False
    if old_lvl != new_lvl:
        return new_lvl, True


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
        sprite_list.clear(screen, background)
        sprite_list.draw(spriteground) 
        screen.blit(spriteground, (0,0))
        pygame.display.update()


if __name__ == '__main__':
    game_cycle()
