#### imports #######################################################
import pygame
from wallcon import *
import levelclasses as levels
from player import Player
from pygame.locals import *
from filereader import readimagesfile



#### main function #################################################
def main():
    #### pre-loop preparations ####

    # activate pygame
    pygame.init()

    # activate screen and define dimensions
    screen = pygame.display.set_mode(WINS)

    # set game screen caption
    pygame.display.set_caption('Platformer')
    
    # set up image library and images
    ifolder = readimagesfile('imagekeys.txt')
    print ifolder

    # set up player
    player = Player(ifolder['ball'])

    # create each level
    levellist = []
    levellist.append(levels.Level01(player))
    levellist.append(levels.Level02(player))

    # set current level
    lvlnum = 0
    lvlnow = levellist[lvlnum]

    # create sprite groups for managing sprites
    spritesunited = pygame.sprite.Group()
    
    # pass in current level class to player
    player.level = lvlnow

    # set player position
    player.rect.x = 360
    player.rect.y = WINH - player.rect.h

    # then add player to sprite list
    spritesunited.add(player)

    # create main loop bool
    done = False

    # set up a clock to manage screen refresh rate
    clock = pygame.time.Clock()

    #### main loop ################################################
    while not done:
        #### event handling loop ####
        
        # retrieve user actions/events
        for event in pygame.event.get():
            # if window close button clicked
            if event.type == pygame.QUIT:
                done = True
            # if a key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_LEFT:
                    player.leftmotion()
                if event.key == pygame.K_RIGHT:
                    player.rightmotion()
                if event.key == pygame.K_UP:
                    player.jump()
            # if a key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.dx < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.dx > 0:
                    player.stop()

        # update sprites
        spritesunited.update()

        # update level
        lvlnow.update()

        # for the following, rgap and lgap are from wallcon
        
        # move background left when player approaches right edge
        if player.rect.right >= rgap:
            diff = player.rect.right - rgap
            player.rect.right = rgap
            lvlnow.worldrevolution(-diff,0)

        # move background right when player approaches left edge
        if player.rect.left <= lgap:
            diff = lgap - player.rect.left
            player.rect.left = lgap
            lvlnow.worldrevolution(diff,0)

        #### moving between levels ################################
        
        # track how far across level player has gone
        posnow = player.rect.x + lvlnow.worldxshift
        # upon reaching the right edge
        if posnow < lvlnow.xshiftmax:
            # reposition
            player.rect.x = 360
            # move to next level
            if lvlnow < len(levellist) - 1:
                lvlnum += 1
                lvlnow = levellist[lvlnum]
                player.level = lvlnow

        #### draw to screen object#################################
    
        # draw background of level first
        lvlnow.draw(screen)
        # then draw sprites to screen
        spritesunited.draw(screen)

        #### clock ################################################
        clock.tick(FPS)

        #### refresh actual screen ################################
        pygame.display.update()

    # exit pygame
    pygame.quit()

# end of main loop

if __name__ == '__main__':
    main()

