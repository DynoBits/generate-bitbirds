# Random functions library
from random import randint

# Numpy library to work with arrays: https://numpy.org/
import numpy as np

BLACK = (0,0,0)
NON_ZERO_BLACK = (10,10,10)
WHITE = (255,255,255)
LIGHT_WHITE = (238,238,238)
GREY = (152,152,152)
LIGHT_GREY = (177.75,177.75,177.75)
LIGHT_LIGHT_GREY = (197,197,197)

RED = (255,0,0)
ORANGE = (255,128,0)
YELLOW = (255,255,0)
GREEN = (0,128,0)
BLUE = (0,0,255)
INDIGO = (75,0,130)
VIOLET = (238,130,238)
RAINBOW = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]

LIGHT_VIOLET = (148,0,211)
AQUA = (0,255,255)
BLUEVIOLET = (138,43,226)

BLOOD = (255,69,0)
SMOKE = (175,175,175)
GRASS = (124,252,0)
BRICK = (156,102,31)
    
# Used as static for diurnal dyno
COLOR_LIST_LIGHT_GREYS = [(250,250,250), (240,240,240), (230,230,230), (220,220,220), (210,210,210), (200,200,200), (190,190,190), (180,180,180)]    
# Used as static for nocturnal dyno
COLOR_LIST_DARK_GREYS = [(70,70,70), (60,60,60), (50,50,50), (40,40,40), (30,30,30), (20,20,20), (10,10,10), (0,0,0)]

def random_color():
    """ Generates random color rgb between (0, 0, 0) and (255, 255, 255) inclusive """
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def lighter(color, percent=0.25):
    """ Returns RGB color percent lighter """
    color = np.array(color)
    vector = WHITE-color
    return tuple(color + vector * percent)

def darker(color, percent=0.25):
    """ Returns RGB color percent darker """
    color = np.array(color)
    black = np.array(NON_ZERO_BLACK)
    vector = black-color
    return tuple(color + vector * percent)

def interval(start_color, end_color, n):
    """
    Returns list of 'n' RGB colors with each element evenly spaced 
    from 'start_color' to 'end_color' respectively
    """
    return list(zip(
        np.linspace(start_color[0], end_color[0], n, dtype = int).tolist(),
        np.linspace(start_color[1], end_color[1], n, dtype = int).tolist(),
        np.linspace(start_color[2], end_color[2], n, dtype = int).tolist(),
        ))
