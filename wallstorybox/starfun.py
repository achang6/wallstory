import pygame
import os
from wallconstants import *
import platform
import readfiles
import user


# create levels object
levels = readfiles.Readmapsfile('starPusherLevels.txt')


def plats_assemble(lvl = 0):
    lvl_width  = levels[lvl]['width']
    lvl_height = levels[lvl]['height']
    h_width    = lvl_width / 2 * TILEW
    h_height   = lvl_height / 2 * TILEF

    for x in range(lvl_width):
        for y in range(lvl_height):
            if levels[lvl]['map_object'][x][y] == '#':
                plat_x = x * TILEW + HWINW - h_width  # + HTILEW
                plat_y = y * TILEF + HWINH - h_height # + HTILEF

                plats = platform.Platform((plat_x, plat_y), sprite_lib['corner'])


def lvl_changed(old_lvl, new_lvl):
    if old_lvl == new_lvl:
        return old_lvl, False
    if old_lvl != new_lvl:
        return new_lvl, True

def activate_monkey(lvl = 0):
    hlvlw = levels[lvl]['width']  / 2
    hlvlh = levels[lvl]['height'] / 2
    
    monkey_x = levels[lvl]['xy_state']['user'][0]
    monkey_x = monkey_x * TILEW + HWINW - hlvlw
    monkey_y = levels[lvl]['xy_state']['user'][1]
    monkey_y = monkey_y * TILEH + HWINH - hlvlh

    return monkey_x, monkey_y
