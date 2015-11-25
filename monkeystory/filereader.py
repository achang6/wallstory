import os
import pygame



def readmapsfile(filename):
    assert os.path.exists(filename), 'Cannot find the levels file: %s' % (filename)

    # parse text file
    levelsfile = open(filename, 'r')
    content = levelsfile.readlines() + ['\r\n']
    levelsfile.close()

    # initiate containers
    levels = []         # list of levels
    plats = []          # list of platforms'  data for a level
    platform = []       # a platform's 5 specs xywhc
    loading = []        # prepares xywhc to store in platform
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
                for c in range(len(plats[l])):
                    # parse
                    if plats[l][c] != ' ':
                        strval += plats[l][c]
                    elif plats[l][c] == ' ' and platspec != 4:
                        loading.append(int(strval))
                        # reset and step
                        strval = ''
                        platspec += 1
                    # quick fix for parameter 5
                    elif plats[l][c] == ' ' and platspec == 4:
                        loading.append(strval)
                        strval = ''
                        platspec = 0
                        platform.append(loading)
                        loading = []
            # store level, reset platform, step
            levels.append(platform)
            platform = []       
            loading = []
            plats = []
            
    # each levels index is a list of platforms
    # 'platform' holds all the platforms of a level
    # each platform index has a platform's data
    # index 01234 is xywhc data respectively
    return levels



def readplayerfile(filename):
    assert os.path.exists(filename), 'Cannot find the levels file: %s' % (filename)

    # parse text file
    levelsfile = open(filename, 'r')
    content = levelsfile.readlines() + ['\r\n']
    levelsfile.close()

    # initiate containers
    clevel = []         # temp container of line in text
    player = []         # list of player start positions each level
    loading = []        # prepares xy to store in player
    playerspec = 0      # player spec index (x,y)
    strval = ''         # temporary string container
    
    # processing levels file
    for i in range(len(content)):
        line = content[i].rstrip('\r\n')

        # comment, turn line into blank if so
        if '#' in line: 
            line = line[:line.find('#')]

        # content, record
        if line != '':
            clevel.append(line + ' ')

        # stop between levels
        elif line == '' and len(clevel) > 0:
            print(clevel)
            # process each line c:character
            for c in range(len(clevel[0])):
                # parse
                if clevel[0][c] != ' ':
                    strval += clevel[0][c]
                elif clevel[0][c] == ' ' and playerspec != 1:
                    loading.append(int(strval))
                    # reset and step
                    strval = ''
                    playerspec += 1
                # quick fix for parameter 2
                elif clevel[0][c] == ' ' and playerspec == 1:
                    loading.append(int(strval))
                    strval = ''
                    playerspec = 0
                    player.append(loading)
                    loading = []       
            loading = []
            clevel = []
    # list of player xy tuples
    return player



def readmapsize(filename):
    assert os.path.exists(filename), 'Cannot find the map size file: %s' % (filename)

    # parse text file
    levelsfile = open(filename, 'r')
    content = levelsfile.readlines() + ['\r\n']
    levelsfile.close()

    # initiate containers
    currentlevel = []           # holds line of text of level
    mapsize = []                # list of true map size
    loading = []                # prepares data to store 
    mapspec = 0              # map size spec index
    strval = ''                 # temporary string container

    # process map size file
    for i in range(len(content)):
        line = content[i].rstrip('\r\n')

        # comment, turn line into blank
        if '#' in line:
            line = line[:line.find('#')]

        # content, record
        if line != '':
            currentlevel.append(line + ' ')
            
        # stop between levels
        elif line == '' and len(currentlevel) > 0:
            # process each line character
            for c in range(len(currentlevel[0])):
                #parse
                if currentlevel[0][c] != ' ':
                    strval += currentlevel[0][c]
                elif currentlevel[0][c] == ' ' and mapspec != 1:
                    loading.append(int(strval))
                    strval = ''
                    mapspec += 1
                elif currentlevel[0][c] == ' ' and mapspec == 1:
                    loading.append(int(strval))
                    strval = ''
                    mapspec = 0
                    mapsize.append(loading)
                    loading = []
            loading = []
            currentlevel = []
    return mapsize




def readimagesfile(filename):
    assert os.path.exists(filename), 'Cannot find the image text file: %s' %(filename)
    
    # parse text file
    imagelist = open(filename, 'r')
    guts = imagelist.readlines() + ['\r\n']
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
    
    # load images
    for i in range(len(imagekey)):
        imagecat[imagekey[i]] = pygame.image.load(imagepath[i])
    
    # results in image dictionary
    return imagecat
