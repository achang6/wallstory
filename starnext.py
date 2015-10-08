# import modules
import pygame, os
import readfiles  # Readmapsfile, Readimagesfile
from wallconstants import *        # constants: FPS, WINW, WINH, TILEW, TILEH, TILEF, lowercase colors


pygame.init()                                                           # initiate pygame
pygame.display.set_caption('Wallstory 0')                               # set window caption
screen = pygame.display.set_mode((WINW, WINH))         # set window surface object
background = pygame.Surface(screen.get_size()).convert()      # set background surface, convert for blitting
background.fill(green)                                             # OPTIONAL: color the background
sprite_dictionary = readfiles.Readimagesfile('starnext_images.txt')     # set image dictionary
level_layouts = readfiles.Readmapsfile('starPusherLevels.txt')            # set levels array/dictionary
clock = pygame.time.Clock()                                        # set pygame clock
playtime = 0.0                                                     # OPTIONAL: container for time app active
font = pygame.font.SysFont('mono', 12, bold = True)                # set font
sprite_list     = pygame.sprite.Group()
platform_list   = pygame.sprite.Group()
for x in level_layouts['map']:
    for y in level_layouts['map'][x]:
        if level_layouts['map'][x][y] == '#':
            platform = Platform(sprite_dictionary['corner'],level_layouts['map'][x],level_layouts['map'][x][y])
            platform_list.add(platform)


def game_cycle():
    Playing = True
    currentLevel = 0
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


class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        self.image   = image
        self.rect = self.image.get_rect
        self.rect.x = x
        self.rect.y = y
    

class User(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        self.image = image
        self.rect     = self.image.get_rect()
        self.rect.x   = x
        self.rect.y   = y
        self.x_shift  = 0
        self.y_shift  = 0
        self.walls    = None
    def accelerate(self, x, y):
        self.x_shift += x
        self.y_shift += y
    def update(self):
        # horizontal
        self.rect.x += self.x_shift
        wall_collision_container = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in wall_collision_container:
            if self.x_shift > 0:
                self.rect.right = wall.rect.left
            elif self.x_shift < 0:
                self.rect.left = wall.rect.right
        # vertical
        self.rect.y += self.y_shift
        wall_collision_container = pygame.sprite.spritecollid(self, self.walls, False)
        for wall in wall_collision_container:
            if self.y_shift > 0:
                self.rect.bottom = wall.rect.top
            elif self.y_shift < 0:
                self.rect.top = wall.rect.bottom







if __name__ == '__main__':
    HelloWorld().run()