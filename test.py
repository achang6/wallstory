import os
import pygame
import readfiles
levels = readfiles.Readmapsfile('starPusherLevels.txt')

for x in range(levels[0]['width']):
    for y in range(levels[0]['height']):
        if levels[0]['map_object'][x][y] == '#':
            print(levels[0]['map_object'][x][y])

