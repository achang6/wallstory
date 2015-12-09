# list of constants

# colors 
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
RED     = (255,  0,  0)
GREEN   = (  0,255,  0)
BLUE    = (  0,  0,255)
BGC     = WHITE
SWAMP   = (165,170,195)
PORTAL  = (245,245,255)

# common constants
PI = 3.141592653

# layout constants
WINW  = 1028
WINH  = 720
WINS  = (WINW,WINH)
HWINW = WINW // 2
HWINH = WINH // 2
FPS = 30

# game variables
xmovespeed = 10
ymovespeed = 3 * xmovespeed
xbackspeed = xmovespeed * 3 / 7
gap  = WINW // 3
rgap = WINW - gap
lgap = gap
tgap = WINH // 5
bgap = WINH * 4 // 5
