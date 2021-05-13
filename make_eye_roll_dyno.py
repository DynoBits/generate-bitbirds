import dyno_colors as dc
from dyno_bit import DynoBit
from dyno_gif import make_temp_file_names, remove_temp_files, save_dyno_gif

# Numpy library to work with arrays: https://numpy.org/
import numpy as np

import copy


def make_eye_roll_dyno(gif_name, dyno=DynoBit()):
    frame_count = 4 # Because the eye is made of 4 bits (a nibble!)
    old_index_list = [(7,17), (6,17), (6,16), (7,16)]
    new_index_list = old_index_list[1:] + [old_index_list[0]]

    temp_file_names = make_temp_file_names(frame_count, "temp_eye_roll")

    if not frame_count == len(old_index_list) == len(new_index_list) == len(temp_file_names):
        raise ValueError(f"frame_count inconsistent: {frame_count} {len(old_index_list)} {len(new_index_list)} {len(temp_file_names)}")

    new_pixels = dyno.pixels()
    old_pixels = dyno.pixels()
    for file in temp_file_names:
        dyno.save_dyno_image(pixel_array=new_pixels, imgname=file)
        for i in range(frame_count): # Move pupil one position
            new_pixels[new_index_list[i]] = old_pixels[old_index_list[i]]
        old_pixels = np.copy(new_pixels) 

    save_dyno_gif(gif_name, temp_file_names+[temp_file_names[0]], bounce=True, fps=8)

    remove_temp_files(temp_file_names)
