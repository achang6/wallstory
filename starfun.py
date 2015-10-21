import pygame
import os
from wallconstants import *
import platform
import readfiles



# create image dictionary
sprite_lib = readfiles.Readimagesfile('starnext_images.txt')
# create levels object
levels = readfiles.Readmapsfile('starPusherLevels.txt')



def plats_assemble(lvl = 0, platforms, sprites):
    lvl_width  = levels[lvl]['width']
    lvl_height = levels[lvl]['height']
    h_width    = lvl_width / 2 * TILEW
    h_height   = lvl_height / 2 * TILEF

    platforms.empty()
    sprites.empty()

    for x in range(width):
        for y in range(height):
            if levels[lvl]['map_object'][x][y] == '#':
                plat_x = TILEW * x + HWINW - h_width  + HTILEW
                plat_y = TILEF * y + HWINH - h_height + HTILEF

                plats = platform.Platform((plat_x, plat_y), sprite_lib['corner'])

                platforms.add(plats)
                sprite_list.add(plats)

def level_changed(old_lvl, new_lvl):
    if old_lvl == new_lvl:
        return old_lvl, False
    if old_lvl != new_lvl:
        return new_lvl, True
