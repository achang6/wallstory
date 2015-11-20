import pygame
from wallcon import *
from pygame.locals import *


#### set-up zone ##################################################
# initiate pygame
pygame.init()

# initiate pygame window
screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('Wallstory')

# set up clock
clock = pygame.time.Clock()

# read data from text zone
# ....

#### function zone ################################################
# ....

#### main-loop zone ###############################################
while not done: 

    # main-loop set up #
    if loading: 
        
