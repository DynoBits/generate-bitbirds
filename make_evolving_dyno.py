import dyno_colors as dc
from dyno_bit import DynoBit
from dyno_gif import make_temp_file_names, remove_temp_files, save_dyno_gif

# Numpy library to work with arrays: https://numpy.org/
import numpy as np

import copy


def make_evolving_dyno(gif_name, from_dyno=None, to_dyno=None, frame_count=10):
    if from_dyno is None and to_dyno is None:
        from_dyno = DynoBit()
        from_dyno.randomize()
        to_dyno = DynoBit()
        to_dyno.randomize()
    if from_dyno != None and to_dyno is None:
        to_dyno = copy.copy(from_dyno)
    if from_dyno is None and to_dyno != None:
        from_dyno = copy.copy(to_dyno)

    if from_dyno.ROWS is not to_dyno.ROWS or from_dyno.COLUMNS is not to_dyno.COLUMNS:
        raise ValueError(f"from_dyno dimensions != to_dyno dimensions: {(from_dyno.ROWS, from_dyno.COLUMNS)} - {(to_dyno.ROWS, to_dyno.COLUMNS)}")

    # Set species for evolution: Euoplocephalus & T-Rex evolve into Euoplorex
    if from_dyno.species == "Euoplocephalus" or from_dyno.species == "T-Rex":
    	setattr(to_dyno, "species", "Euoplorex")
    elif to_dyno.species == "Euoplocephalus" or to_dyno.species == "T-Rex":
    	setattr(from_dyno, "species", "Euoplorex")
    else:
    	setattr(from_dyno, "species", "Euoplocephalus")

    # Make ROWSxCOLUMS list of list containing interval color of each pixel
    dyno_pixels_intervals = []
    from_dyno_pixels = from_dyno.pixels()
    to_dyno_pixels = to_dyno.pixels()
    for r in range(to_dyno.ROWS):
        for c in range(to_dyno.COLUMNS):
            from_dyno_pixels
            dyno_pixels_intervals += [ dc.interval(from_dyno_pixels[r,c], to_dyno_pixels[r,c], frame_count) ]

    # Use list of intervals to make each dyno frame
    temp_file_names = make_temp_file_names(frame_count, "temp_evolving")
    for i in range(frame_count):
        new_dyno_pixels = np.array( [ [(0,0,0)]*to_dyno.ROWS ]*to_dyno.COLUMNS, dtype=np.uint8)

        i_dpi = 0
        for r in range(to_dyno.ROWS):
            for c in range(to_dyno.COLUMNS):
                new_dyno_pixels[r,c] = tuple(dyno_pixels_intervals[i_dpi][i])
                i_dpi += 1

        from_dyno.save_dyno_image(new_dyno_pixels, imgname=temp_file_names[i])

    save_dyno_gif(gif_name, temp_file_names+[temp_file_names[-1]], bounce=True)

    remove_temp_files(temp_file_names)
