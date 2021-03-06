import os
import pygame


def Readmapsfile(filename):
    # make sure map file exists
    assert os.path.exists(filename), ' Cannot find the levels file: %s' %(filename)

    # open, read, close file
    map_file = open(filename, 'r')
    guts = map_file.readlines() + ['\r\n']
    map_file.close()

    # containers assemble
    levels = []         # list of level objects
    level_num = 0       # index of current map/level
    map_lines = []      # list of strings of each map line
    map_object = []     # object?
    
    # processing
    for line_num in range(len(guts)):
        line = guts[line_num].rstrip('\r\n')

        # ; = comment, remove from guts
        if ';' in line:
            line = line[:line.find(';')]

        # map line
        if line != '':
            map_lines.append(line)

        # end of a map/level
        elif line == '' and len(map_lines) > 0:
            # make all lines in map the same width
            max_width = -1
            # find widest line's width
            for i in range(len(map_lines)):
                if len(map_lines[i]) > max_width:
                    max_width = len(map_lines[i])

            # add blanks until each line as long as widest
            for i in range(len(map_lines)):
                map_lines[i] += ' ' * (max_width - len(map_lines[i]))

            # make map object
            for x in range(len(map_lines[0])):                  
                map_object.append([])                           # add x amount of columns
            for y in range(len(map_lines)):                  # row
                for x in range(max_width):                      # column in row
                    map_object[x].append(map_lines[y][x])       # add column value for that row

            # character processing
            x_start = None
            y_start = None
            for x in range(max_width):
                for y in range(len(map_object[x])):
                    if map_object[x][y] in ('@', '+'):
                        # '@' represent player in text map
                        x_start = x
                        y_start = y

            # existence
            assert x_start != None and y_start != None, 'Level %s in %s missing the start point "@" or "+"' % (level_num +1, filename)
            
            # create level object
            game_object  = {'user': (x_start, y_start)}
            level_object = {'width': max_width,
                    'height': len(map_object[0]),
                    'map_object': map_object,
                    'xy_state': game_object}
            levels.append(level_object)
            
            # reset variables for next map
            map_lines = []
            map_object = []
            game_object = {}
            level_num += 1
    return levels




def Readimagesfile(filename):
    assert os.path.exists(filename), 'Cannot find the image file: %s' %(filename)
    imagefile = open(filename, 'r')
    guts = imagefile.readlines() + ['\r\n']
    imagefile.close()

    # processing
    imagekey = []
    imagepath = []
    imagecat = {}

    for linenumber in range(len(guts)):
        line = guts[linenumber].rstrip('\r\n')
        if ';' in line:
            imagekey.append(line[1:])
        if '#' in line:
            imagepath.append(line[1:])
        
    imagemonkey = [imagekey,imagepath]
    
    for i in range(len(imagemonkey[0])):
        imagecat[imagemonkey[0][i]] = pygame.image.load(imagemonkey[1][i])
    
    return imagecat
