import pygame
from player import User
from filereader import readmapsfile
from filereader import readplayerfile
from filereader import readmapsize
from pygame.sprite import spritecollide
from pygame.locals import *
from wallcon import * 
from platform import Platform



#### set-up zone ################################################
# initiate pygame
pygame.init()

# initiate pygame window
screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('Wallstory')

# set up clock
clock = pygame.time.Clock()

# read levels data from text
levels = readmapsfile('wallspec.txt')
playpos = readplayerfile('startpos.txt')
mapsizes = readmapsize('wallsizes.txt')
print(mapsizes[0][0])
print(mapsizes[0][1])

# Loop variables:
loading = True          # for function that loads level 
levelindex = 0          # index to track current level

# sprite groups
sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()



#### function zone ############################################
def platsassemble(levelnow,levelindex):
    for p in range(len(levelnow)):
        platform = Platform(levelnow[p])
        platform.harvesthour(mapsizes[levelindex][0],mapsizes[levelindex][1])
        wall_list.add(platform)
        sprite_list.add(platform)
        print(str(levelnow[p]))

def playeradvance(levelnow):
    ball = pygame.image.load('wimages/ball.png')
    player_x = 640 # levelnow[0]
    player_y = 360 # levelnow[1]
    player = User(ball, player_x, player_y)
    player.walls = wall_list
    sprite_list.add(player)
    return player

    

#### main-loop zone ############################################
while not done:
    
    # main loop set up #
    if loading:
        platsassemble(levels[levelindex],levelindex)     
        player = playeradvance(playpos[levelindex])
        loading = False

    #### event handling loop ##################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
            if event.key == K_LEFT:
                dx -= xmovespeed
            if event.key == K_RIGHT:
                dx += xmovespeed
            if event.key == K_UP:
                dy -= ymovespeed
            if event.key == K_DOWN:
                dy += ymovespeed
        elif event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                dx = 0
            if event.key == K_RIGHT:
                dx = 0
            if event.key == K_UP:
                dy = 0
            if event.key == K_DOWN:
                dy = 0

    #### processing ##############################################
    # move the world
    for wall in wall_list:
        wall.worldrevolution(dx,dy)

    #### last words ##############################################
    sprite_list.update()

    screen.fill(BGC)

    sprite_list.draw(screen)

    pygame.display.update()

    clock.tick(FPS)

#### Exit ######################################################
pygame.quit()
