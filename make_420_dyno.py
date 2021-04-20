## Make 420 dyno
"""
Run this script to create the special edition 420 Dyno 
A gif named 420_dyno.gif will appear in the current directory
"""


# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np

from random import choice
from random import randint

# library to interact with the operating system
import os

# For making gif
import imageio


WHITE = (255,255,255)
LIGHT_WHITE = (238,238,238)
GREY = (152,152,152)
LIGHT_GREY = (177.75,177.75,177.75)
LIGHT_LIGHT_GREY = (197,197,197)
BLACK = (0,0,0)
NON_ZERO_BLACK = (10,10,10)
RED = (255,0,0)
BLOOD = (255,69,0)
SMOKE = (175,175,175)
GRASS = (124,252,0)

FRAME_COUNT_FOR_GIF = 10

# Used as static for diurnal dyno
COLOR_LIST_LIGHT_GREYS = [(250,250,250), (240,240,240), (230,230,230), (220,220,220), 
                            (210,210,210), (200,200,200), (190,190,190), (180,180,180)]


"""Returns RGB color percent lighter"""
def lighter(color, percent=0.25):
    color = np.array(color)
    vector = WHITE-color
    return tuple(color + vector * percent)


"""Returns RGB color percent darker"""
def darker(color, percent=0.25):
    color = np.array(color)
    black = np.array(NON_ZERO_BLACK)
    vector = black-color
    return tuple(color + vector * percent)


"""Returns a DynoBit image with specified attributes
pixels = 24x24 np.array of colors (from make_dyno_image())
imgname = name/location to wright final dyno to
dimensions = dimensions of image to write
"""
def save_dyno_image(pixels, imgname, dimensions=(480, 480)):
    new_image = Image.fromarray(pixels)
    new_image = new_image.resize(dimensions, resample=0)
    new_image.save(imgname)


"""
png_frames = list of strings of png files
bounce = true: gif bounces frames false: gif repeats frames 
fps = framse per second
"""
def save_dyno_gif_new(write_dir, png_frames, bounce=True, fps=10):
    if write_dir[-4:] != ".gif":
        raise ValueError("Save gif dir doesnt end with .gif!")

    # Make gif file names
    gif_file_names = list.copy(png_frames)
    if bounce:
        gif_file_names.extend(reversed(gif_file_names))

    # Write gif
    imageio.mimsave(write_dir, [imageio.imread(f) for f in gif_file_names], fps=fps)


"""Returns a DynoBit image with specified attributes"""
def make_dyno_image(
        emotion="Angry",
        species="Euoplocephalus",
        activity="Diurnal",
        background_color=LIGHT_WHITE, 
        outline_color=BLACK, 
        eyebrow_color=BLACK, 
        limbs_color=GREY, 
        sclera_color=WHITE, 
        pupil_color=BLACK, 
        skin_color=LIGHT_LIGHT_GREY, 
        horn_color=GREY, 
        spike1_color=GREY, spike2_color=GREY, spike3_color=GREY, spike4_color=GREY, 
        tail_color=GREY, 
        spot1_in_color=GREY, spot1_out_color=LIGHT_GREY, spot2_in_color=GREY, spot2_out_color=LIGHT_GREY, spot3_in_color=GREY, spot3_out_color=LIGHT_GREY, spot4_in_color=GREY, spot4_out_color=LIGHT_GREY, spot5_in_color=GREY, spot5_out_color=LIGHT_GREY):
    # Set colors
    bg = background_color
    ol = outline_color
    eb = eyebrow_color
    al = limbs_color
    sc = sclera_color
    pu = pupil_color
    sk = skin_color
    hn = horn_color
    s1,s2,s3,s4 = spike1_color,spike2_color,spike3_color,spike4_color
    tl = tail_color
    i1,i2,i3,i4,i5 = spot1_in_color,spot2_in_color,spot3_in_color,spot4_in_color,spot5_in_color
    o1,o2,o3,o4,o5 = spot1_out_color,spot2_out_color,spot3_out_color,spot4_out_color,spot5_out_color

    # Activity
    if activity == "Nocturnal": 
        bg,ol = ol,bg


    if species == "Euoplocephalus":
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
    elif species == "T-Rex":
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
    elif species == "Euoplorex":
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
        raise ValueError("Species not specified correctly")

    if emotion == "Angry":
        eb_rows = [4, 5]
        eb_cols = [6, 5]
    elif emotion == "Happy":
        eb_rows = [4, 5]
        eb_cols = [7, 8]
    elif emotion == "Neutral":
        eb_rows = [4, 4]
        eb_cols = [6, 7]
    else:
        raise ValueError("Emotion not specified correctly")

    dyno_pixels[eb_rows, eb_cols] = eb
    return np.fliplr(dyno_pixels)


def make_smoking_dyno(imgname, base_dyno):
    frame_count = 10
    temp_file_names = [f"{os.getcwd()}/temp_smoking{i}.png" for i in range(frame_count)]

    # Bloodshot eyes cuz Dyno high af
    base_dyno[[6, 6, 7], [17, 16, 16]] = (255,69,0)

    curr_frame = 0
    # put blunt
    blunt_color = (156,102,31) # Brick
    base_dyno[12, [20, 21, 22]] = blunt_color
    base_dyno[12, 22] = RED
    save_dyno_image(base_dyno, temp_file_names[curr_frame])

    curr_frame = 1
    working_dyno = np.copy(base_dyno)
    working_dyno[12, 22] = darker(RED, 0.1)
    working_dyno[11, 22] = SMOKE
    save_dyno_image(working_dyno, temp_file_names[curr_frame])

    # V4 - NOTE FAMECOUNT = 10
    curr_frame = 2
    working_dyno = np.copy(base_dyno)
    working_dyno[12, 22] = darker(RED, 0.1)
    working_dyno[[11, 10], [22, 22]] = SMOKE
    save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 3
    working_dyno = np.copy(base_dyno)
    working_dyno[[11, 10, 9], [22, 22, 21]] = SMOKE
    save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 4
    working_dyno = np.copy(base_dyno)
    working_dyno[[11, 10, 8, 9], [22, 22, 21, 22]] = SMOKE
    save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 5
    working_dyno = np.copy(base_dyno)
    working_dyno[12, 22] = darker(RED, 0.1)
    working_dyno[[11, 10, 7, 8, 9], [22, 22, 21, 22, 21]] = SMOKE
    save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 6
    working_dyno = np.copy(base_dyno)
    working_dyno[12, 22] = darker(RED, 0.1)
    working_dyno[[11, 10, 6, 7, 8, 9], [22, 22, 20, 22, 21, 22]] = SMOKE
    save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 7
    working_dyno = np.copy(base_dyno)
    working_dyno[[11, 10, 5, 6, 7, 8, 9], [22, 22, 20, 21, 21, 22, 21]] = SMOKE
    save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 8
    working_dyno = np.copy(base_dyno)
    working_dyno[[11, 10, 4, 5, 6, 5, 7, 8, 9], [22, 22, 19, 20, 21, 22, 22, 21, 22]] = SMOKE
    save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 9
    working_dyno = np.copy(base_dyno)
    working_dyno[12, 22] = darker(RED, 0.1)
    working_dyno[[11, 10, 3, 4, 5, 4, 6, 7, 8, 9], [22, 22, 19, 19, 20, 22, 21, 21, 22, 21]] = SMOKE
    save_dyno_image(working_dyno, temp_file_names[curr_frame])

    # Write gif
    save_dyno_gif_new(imgname, [temp_file_names[0]]+temp_file_names, bounce=False, fps=5)

    # Remove temp files
    for f in temp_file_names:
        os.remove(f)


# ----------------------------------
emotion="Happy"
species="Euoplorex"
activity="Diurnal"
background_color=LIGHT_WHITE
outline_color=BLACK
eyebrow_color=BLACK
limbs_color=BLACK
sclera_color=WHITE
pupil_color=BLACK
skin_color=GRASS
horn_color=(0,75,0)

spike1_color = (0,118,0)
spike2_color = (0,165,0)
spike3_color = (0,205,0)
spike4_color = (0,238,0)
tail_color = (0,255,0)

spot1_in_color = tail_color
spot2_in_color = spike4_color
spot3_in_color = spike3_color
spot4_in_color = spike2_color
spot5_in_color = spike1_color

spot1_out_color = lighter(spot1_in_color)
spot2_out_color = lighter(spot2_in_color)
spot3_out_color = lighter(spot3_in_color)
spot4_out_color = lighter(spot4_in_color)
spot5_out_color = lighter(spot5_in_color)

dyno_420 = make_dyno_image(
    emotion,
    species,
    activity,
    background_color, 
    outline_color, 
    eyebrow_color, 
    limbs_color, 
    sclera_color, 
    pupil_color, 
    skin_color, 
    horn_color, 
    spike1_color, spike2_color, spike3_color, spike4_color, 
    tail_color, 
    spot1_in_color, spot1_out_color, spot2_in_color, spot2_out_color, spot3_in_color, spot3_out_color, spot4_in_color, spot4_out_color, spot5_in_color, spot5_out_color)


# 420 dyno
make_smoking_dyno(f"{os.getcwd()}/420_dyno.gif", dyno_420)
