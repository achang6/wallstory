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
background.fill(green)                                                  # OPTIONAL: color the background
sprite_lib = readfiles.Readimagesfile('starnext_images.txt')     # set image dictionary
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
    platform_list.empty()
    sprite_list.empty()
    for x in range(levels[lvl]['width']):
        for y in range(levels[lvl]['height']):
            if levels[lvl]['map_object'][x][y] == '#':
                plat_x = TILEW * x
                plat_y = TILEF * y
                plats = pygame.sprite.Sprite()
                plats = platform.Platform((plat_x, plat_y), sprite_lib['corner'])
                platform_list.add(plats)
                sprite_list.add(plats)
    
def level_changed(before, after):
    old_lvl = before
    new_lvl = after
    if old_lvl == new_lvl:
        return old_level, False
    if old_lvl != new_lvl:
        return new_lvl, True


def game_cycle():
    Playing = True
    lvl_tracker = lvl
    migrate = False
    plats_assemble(lvl)
    mainmonkey = User(sprite_lib['horngirl'], levels[lvl]['xy_state'][0], levels[lvl]['xy_state'][1])
    mainmonkey.walls = platform_list
    sprite_list.add(mainmonkey)

    # main loop ------------------------------------------------------------
    while Playing:
        # keep track of if level has changed
        lvl_tracker, migrate = level_changed(lvl_tracker, lvl)
        if migrate:
            mainmonkey.walls = platform_list
            sprite_list.add(mainmonkey)
            lvl_width = levels[lvl]['width']
            lvl_height = levels[lvl]['height']
            lvl_object = levels[lvl]['map_object']
            plats_assemble(lvl)

        
        # event handling loop -----------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Playing = False             # exit
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
                if event.key == pygame.K_UP and event.key == pygame.K_RIGHT:
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
                    mainmonkey.accelerate(-pixspeed, pixspeed)
        # work space ------------------------------------------------------

        sprite_list.update()
        sprite_list.clear(background)
        sprite_list.draw(background)
        pygame.display.update()
        self.screen.blit(self.background, (0,0))


if __name__ == '__main__':
    game_cycle()
