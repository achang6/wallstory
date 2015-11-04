import os
import pygame


def readmapsfile(filename):
    assert os.path.exists(filename), 'Cannot find the levels file: %s' % filename)

    # parse text file
    levelsfile = open(filename, 'r')
    content = levelsfile.readlines() + ['\r\n']
    levelsfile.close()

    # initiate containers
    levels = []         # list of levels
    levelnum = 0        # level index
    plats = []          # list of platforms'  data for a level
    platform = []       # a platform's 4 specs xywh
    platspec = 0        # plat spec index
    strval = ''         # temporary string container
    
    # processing levels file
    for i in range(len(content)):
        line = content[i].rstrip('\r\n')

        # comment, turn line into blank if so
        if '#' in line: 
            line = line[:line.find('#')]

        # content, record
        if line != '':
            plats.append(line + ' ')

        # stop between levels
        elif line == '' and len(plats) > 0:    
            # process each level: l:line, c:character
            for l in range(len(plats)):
                for c in len(plats[l]):
                    # parse
                    if plats[l][c] != ' ':
                        strval += plats[l][c]
                    elif plats[l][c] == ' ' and platspec != 4:
                        platform[platspec] = int(strval)
                        # reset and step
                        strval = ''
                        platspec += 1
                    # quick fix for parameter 5
                    elif plats[l][c] == ' ' and platspec == 4:
                        strval = ''
                        platspec = 0
                # reset for next line
                platspec = 0
            # store level, reset platform, step
            levels[levelnum] = platform
            platform = []       
            levelnum += 1
            
    # each levels index is a list of platforms
    # 'platform' holds all the platforms of a level
    # each platform index has a platform's data
    # index 01234 is xywhc data respectively
    return levels



def readimagesfile(filename):
    assert os.path.exists(filename), 'Cannot find the image text file: %s' %(filename)
    
    # parse text file
    imagelist = open(filename, 'r')
    guts = imagefile.readlines() + ['\r\n']
    imagelist.close()

    # lists for processing
    imagekey  = []
    imagepath = []
    imagecat  = {}

    # processing
    for linenum in range(len(guts)):
        line = guts[linenum].rstrip('\r\n')
        if ';' in line:
            # line is key, remove ; and store
            imagekey.append(line[1:])
        if '#' in line:
            # line is directory, remove # and store
            imagepath.append(line[1:])
    
    # QOL variable
    imonkey = [imagekey, imagepath]

    # load images
    for i in range(len(imonkey[0])):
        imagecat[imonkey[0][i]] = pygame.image.load(imonkey[1][i]])
    
    # results in keys for image dictionary
    return imagecat
