"""
DynoBit as an object.
Fully configure every attribute of Dyno in constructor.
Leave empty for defaults.
Even specifiy some attributes in any order.
Then save dyno to any directory with save_dyno_image(imgname=<image_location>).
    EX:
        d = DynoBit()
        d.save_dyno_image()
"""

""" Built with python 3, dependencies installed with pip & homebrew """
# Colors as RGB tuple
import dyno_colors as dc

# Random functions library
from random import choice
from random import randint
from random import seed

# Numpy library to work with arrays: https://numpy.org/
import numpy as np

# Operating system library
import os

# Library for making gif
import imageio

# Library to generate images: https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

import copy

class DynoBit():
    # init method or constructor   
    def __init__(
            self,
            emotion="Angry", 
            species="Euoplocephalus", 
            activity="Diurnal", 
            background_color=dc.LIGHT_WHITE, 
            outline_color=dc.BLACK, 
            eyebrow_color=dc.BLACK, 
            limbs_color=dc.GREY, 
            sclera_color=dc.WHITE, 
            pupil_color=dc.BLACK, 
            skin_color=dc.LIGHT_LIGHT_GREY, 
            horn_color=dc.GREY, 
            tail_color=dc.GREY, 
            spike_color_list=[dc.GREY]*4, 
            spot_in_color_list=[dc.GREY]*5, 
            spot_out_color_list=[dc.LIGHT_GREY]*5,
        ):
        self.emotion = emotion 
        self.species = species
        self.activity = activity
        self.background_color = background_color
        self.outline_color = outline_color
        self.eyebrow_color = eyebrow_color
        self.limbs_color = limbs_color
        self.sclera_color  = sclera_color 
        self.pupil_color = pupil_color
        self.skin_color = skin_color
        self.horn_color  = horn_color 
        self.tail_color = tail_color
        self.spike_color_list = spike_color_list
        self.spot_in_color_list = spot_in_color_list
        self.spot_out_color_list = spot_out_color_list
        self.ROWS, self.COLUMNS = 24, 24


    # TODO: set randomization to match that of generation-script
    def randomize(self):
        self.emotion = choice(["Happy", "Angry", "Neutral"])
        self.species = choice(["Euoplocephalus", "T-Rex", "Euoplorex"])
        self.activity = choice(["Diurnal", "Nocturnal"])
        self.eyebrow_color = dc.random_color()
        self.limbs_color = dc.random_color()
        self.sclera_color  = dc.random_color() 
        self.pupil_color = dc.random_color()
        self.skin_color = dc.random_color()
        self.horn_color  = dc.random_color() 
        self.tail_color = dc.random_color()
        self.spike_color_list = [dc.random_color(), dc.random_color(), dc.random_color(), dc.random_color()]
        self.spot_in_color_list = [dc.random_color(), dc.random_color(), dc.random_color(), dc.random_color(), dc.random_color()]
        self.spot_out_color_list = [dc.lighter(self.spot_in_color_list[0]), dc.lighter(self.spot_in_color_list[1]), dc.lighter(self.spot_in_color_list[2]), dc.lighter(self.spot_in_color_list[3]), dc.lighter(self.spot_in_color_list[4])]


    def pixels(self):
        """ Return 24x24 numpy array of pixel color tuples """
        bg = self.background_color
        ol = self.outline_color
        eb = self.eyebrow_color
        al = self.limbs_color
        sc = self.sclera_color
        pu = self.pupil_color
        sk = self.skin_color
        hn = self.horn_color
        tl = self.tail_color
        s1,s2,s3,s4 = self.spike_color_list[:]
        i1,i2,i3,i4,i5 = self.spot_in_color_list[:]
        o1,o2,o3,o4,o5 = self.spot_out_color_list[:]

        if self.species == "Euoplocephalus":
            dyno_pixels = np.array([
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, hn, bg, bg, bg, hn, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, hn, hn, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, ol, ol, sk, sk, sk, sk, sk, hn, hn, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, hn, hn, hn, sk, sk, sk, ol, s1, bg, bg, bg, bg, bg, bg],
                [bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, s1, s1, bg, bg, bg, bg, bg],
                [bg, bg, ol, sk, sk, sk, sc, sc, sk, sk, sk, sk, sk, sk, sk, sk, ol, s1, bg, bg, bg, bg, bg, bg],
                [bg, bg, ol, sk, sk, sk, pu, sc, sk, sk, sk, sk, sk, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, s2, bg, bg, bg, bg, bg, bg],
                [bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, s2, s2, bg, bg, bg, bg, bg],
                [bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, s2, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, ol, ol, ol, ol, sk, sk, sk, sk, sk, sk, sk, sk, ol, s3, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, s3, s3, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, al, al, ol, sk, sk, sk, al, al, al, sk, sk, sk, ol, s3, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, al, bg, ol, sk, sk, sk, al, sk, sk, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, s4, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, s4, s4, bg, tl, tl, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, s4, bg, bg, tl, tl, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, bg, bg, tl, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, al, al, ol, ol, ol, tl, tl, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, al, al, bg, bg, bg, bg, al, al, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, al, al, al, bg, bg, bg, al, al, al, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
            ], dtype=np.uint8)
        elif self.species == "T-Rex":
            dyno_pixels = np.array([
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, ol, ol, sk, sk, sk, sk, o1, i1, i1, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, ol, ol, sk, sk, sk, sk, sk, sk, sk, o1, o1, o1, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, o2, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, sc, sc, sk, sk, sk, sk, sk, sk, o2, i2, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, pu, sc, sk, sk, sk, sk, sk, sk, o2, i2, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, o2, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, o3, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, ol, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, o3, i3, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, ol, ol, ol, ol, sk, sk, sk, sk, sk, sk, o3, i3, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, o3, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, al, ol, o5, sk, sk, sk, al, al, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, al, al, ol, i5, o5, sk, al, al, sk, sk, sk, sk, o4, ol, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, i5, o5, sk, sk, sk, sk, sk, sk, sk, o4, i4, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, i5, o5, sk, sk, sk, sk, sk, sk, sk, sk, o4, o4, ol, ol, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, o5, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, ol, ol, ol, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, al, al, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, al, al, bg, bg, bg, bg, al, al, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, al, al, bg, bg, bg, bg, al, al, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
            ], dtype=np.uint8)
        elif self.species == "Euoplorex":
            dyno_pixels = np.array([
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, hn, bg, bg, bg, hn, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, hn, hn, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, ol, ol, sk, sk, sk, sk, sk, hn, hn, o1, o1, o1, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, hn, hn, hn, sk, sk, sk, ol, s1, bg, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, o2, ol, s1, s1, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, sc, sc, sk, sk, sk, sk, sk, sk, o2, i2, ol, s1, bg, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, pu, sc, sk, sk, sk, sk, sk, sk, o2, i2, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, o2, ol, s2, bg, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, s2, s2, bg, bg, bg, bg, bg],
                [bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, o3, ol, s2, bg, bg, bg, bg, bg, bg],
                [bg, bg, ol, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, o3, i3, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, ol, ol, ol, ol, sk, sk, sk, sk, sk, sk, o3, i3, ol, s3, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, o3, ol, s3, s3, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, al, ol, o5, sk, sk, sk, al, al, sk, sk, sk, ol, s3, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, al, al, ol, i5, o5, sk, al, al, sk, sk, sk, o4, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, i5, o5, sk, sk, sk, sk, sk, o4, i4, ol, s4, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, i5, o5, sk, sk, sk, sk, sk, o4, i4, ol, s4, s4, bg, tl, tl, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, o5, sk, sk, sk, sk, sk, sk, sk, o4, ol, s4, bg, bg, tl, tl, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, bg, bg, tl, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, al, al, ol, ol, ol, tl, tl, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, al, al, bg, bg, bg, bg, al, al, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, al, al, al, bg, bg, bg, al, al, al, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
            ], dtype=np.uint8)
        else:
            raise ValueError(f"Species not specified correctly: {self.species}")
    
        if self.emotion == "Angry":
            eb_rows = [4, 5]
            eb_cols = [6, 5]
        elif self.emotion == "Happy":
            eb_rows = [4, 5]
            eb_cols = [7, 8]
        elif self.emotion == "Neutral":
            eb_rows = [4, 4]
            eb_cols = [6, 7]
        else:
            raise ValueError(f"Emotion not specified correctly: {self.emotion}")
    
        dyno_pixels[eb_rows, eb_cols] = eb
        return np.fliplr(dyno_pixels)


    def save_dyno_image(self, pixel_array=None, imgname=f"{os.getcwd()}/dyno_image.png", dimensions=(480, 480)):
        """ Saves DynoBit object as png image a DynoBit image with specified attributes """
        if pixel_array is None:
            pixel_array = self.pixels()
        new_image = Image.fromarray(pixel_array)
        new_image = new_image.resize(dimensions, resample=0)
        new_image.save(imgname)

    def get_background_index_list(self):
        """ Returns a list of all background indices - used in make_static_dyno """
        if self.species == "Euoplocephalus":
            return [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (0, 19), (0, 20), (0, 21), (0, 22), (0, 23), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 14), (1, 15), (1, 16), (1, 18), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 19), (2, 20), (2, 21), (2, 22), (2, 23), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 21), (3, 22), (3, 23), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 22), (4, 23), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 22), (5, 23), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 22), (6, 23), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 22), (7, 23), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 22), (8, 23), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 22), (9, 23), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 22), (10, 23), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 21), (11, 22), (11, 23), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 20), (12, 21), (12, 22), (12, 23), (13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (13, 18), (13, 19), (13, 20), (13, 21), (13, 22), (13, 23), (14, 0), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 20), (14, 21), (14, 22), (14, 23), (15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 18), (15, 20), (15, 21), (15, 22), (15, 23), (16, 0), (16, 1), (16, 2), (16, 3), (16, 4), (16, 5), (16, 18), (16, 19), (16, 20), (16, 21), (16, 22), (16, 23), (17, 0), (17, 1), (17, 4), (17, 18), (17, 19), (17, 20), (17, 21), (17, 22), (17, 23), (18, 0), (18, 1), (18, 4), (18, 5), (18, 18), (18, 19), (18, 20), (18, 21), (18, 22), (18, 23), (19, 0), (19, 1), (19, 2), (19, 3), (19, 5), (19, 6), (19, 18), (19, 19), (19, 20), (19, 21), (19, 22), (19, 23), (20, 0), (20, 1), (20, 2), (20, 3), (20, 4), (20, 18), (20, 19), (20, 20), (20, 21), (20, 22), (20, 23), (21, 0), (21, 1), (21, 2), (21, 3), (21, 4), (21, 5), (21, 6), (21, 7), (21, 8), (21, 9), (21, 12), (21, 13), (21, 14), (21, 15), (21, 18), (21, 19), (21, 20), (21, 21), (21, 22), (21, 23), (22, 0), (22, 1), (22, 2), (22, 3), (22, 4), (22, 5), (22, 6), (22, 7), (22, 8), (22, 9), (22, 13), (22, 14), (22, 15), (22, 19), (22, 20), (22, 21), (22, 22), (22, 23), (23, 0), (23, 1), (23, 2), (23, 3), (23, 4), (23, 5), (23, 6), (23, 7), (23, 8), (23, 9), (23, 10), (23, 11), (23, 12), (23, 13), (23, 14), (23, 15), (23, 16), (23, 17), (23, 18), (23, 19), (23, 20), (23, 21), (23, 22), (23, 23)]
        if self.species == "T-Rex":
        	return [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (0, 19), (0, 20), (0, 21), (0, 22), (0, 23), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 17), (1, 18), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 19), (2, 20), (2, 21), (2, 22), (2, 23), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 21), (3, 22), (3, 23), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 22), (4, 23), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 23), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 23), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 23), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 23), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 23), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 23), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 22), (11, 23), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 20), (12, 21), (12, 22), (12, 23), (13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (13, 5), (13, 6), (13, 18), (13, 19), (13, 20), (13, 21), (13, 22), (13, 23), (14, 0), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), (14, 19), (14, 20), (14, 21), (14, 22), (14, 23), (15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 20), (15, 21), (15, 22), (15, 23), (16, 0), (16, 1), (16, 2), (16, 3), (16, 4), (16, 18), (16, 19), (16, 20), (16, 21), (16, 22), (16, 23), (17, 0), (17, 1), (17, 2), (17, 18), (17, 19), (17, 20), (17, 21), (17, 22), (17, 23), (18, 0), (18, 1), (18, 18), (18, 19), (18, 20), (18, 21), (18, 22), (18, 23), (19, 0), (19, 1), (19, 2), (19, 18), (19, 19), (19, 20), (19, 21), (19, 22), (19, 23), (20, 0), (20, 1), (20, 2), (20, 3), (20, 4), (20, 5), (20, 6), (20, 18), (20, 19), (20, 20), (20, 21), (20, 22), (20, 23), (21, 0), (21, 1), (21, 2), (21, 3), (21, 4), (21, 5), (21, 6), (21, 7), (21, 8), (21, 9), (21, 10), (21, 13), (21, 14), (21, 15), (21, 16), (21, 19), (21, 20), (21, 21), (21, 22), (21, 23), (22, 0), (22, 1), (22, 2), (22, 3), (22, 4), (22, 5), (22, 6), (22, 7), (22, 8), (22, 9), (22, 10), (22, 11), (22, 14), (22, 15), (22, 16), (22, 17), (22, 20), (22, 21), (22, 22), (22, 23), (23, 0), (23, 1), (23, 2), (23, 3), (23, 4), (23, 5), (23, 6), (23, 7), (23, 8), (23, 9), (23, 10), (23, 11), (23, 12), (23, 13), (23, 14), (23, 15), (23, 16), (23, 17), (23, 18), (23, 19), (23, 20), (23, 21), (23, 22), (23, 23)]
        if self.species == "Euoplorex":
            return [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (0, 19), (0, 20), (0, 21), (0, 22), (0, 23), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 14), (1, 15), (1, 16), (1, 18), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 19), (2, 20), (2, 21), (2, 22), (2, 23), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 21), (3, 22), (3, 23), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 22), (4, 23), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 23), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 23), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 23), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 23), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 23), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 23), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 22), (11, 23), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 20), (12, 21), (12, 22), (12, 23), (13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (13, 18), (13, 19), (13, 20), (13, 21), (13, 22), (13, 23), (14, 0), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 19), (14, 20), (14, 21), (14, 22), (14, 23), (15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 20), (15, 21), (15, 22), (15, 23), (16, 0), (16, 1), (16, 2), (16, 3), (16, 4), (16, 5), (16, 18), (16, 19), (16, 20), (16, 21), (16, 22), (16, 23), (17, 0), (17, 1), (17, 4), (17, 18), (17, 19), (17, 20), (17, 21), (17, 22), (17, 23), (18, 0), (18, 1), (18, 4), (18, 5), (18, 18), (18, 19), (18, 20), (18, 21), (18, 22), (18, 23), (19, 0), (19, 1), (19, 2), (19, 3), (19, 5), (19, 6), (19, 18), (19, 19), (19, 20), (19, 21), (19, 22), (19, 23), (20, 0), (20, 1), (20, 2), (20, 3), (20, 4), (20, 18), (20, 19), (20, 20), (20, 21), (20, 22), (20, 23), (21, 0), (21, 1), (21, 2), (21, 3), (21, 4), (21, 5), (21, 6), (21, 7), (21, 8), (21, 9), (21, 12), (21, 13), (21, 14), (21, 15), (21, 18), (21, 19), (21, 20), (21, 21), (21, 22), (21, 23), (22, 0), (22, 1), (22, 2), (22, 3), (22, 4), (22, 5), (22, 6), (22, 7), (22, 8), (22, 9), (22, 13), (22, 14), (22, 15), (22, 19), (22, 20), (22, 21), (22, 22), (22, 23), (23, 0), (23, 1), (23, 2), (23, 3), (23, 4), (23, 5), (23, 6), (23, 7), (23, 8), (23, 9), (23, 10), (23, 11), (23, 12), (23, 13), (23, 14), (23, 15), (23, 16), (23, 17), (23, 18), (23, 19), (23, 20), (23, 21), (23, 22), (23, 23)]
        else:
            raise ValueError("youre stupid")

    def __cmp__(self):
        return cmp(self)
