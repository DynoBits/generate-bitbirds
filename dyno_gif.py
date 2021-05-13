# library to interact with the operating system
import os

# For making gif
import imageio


def make_temp_file_names(file_count, file_base="temp"):
    """ Make a list of temp file names """
    return [f"{os.getcwd()}/{file_base}{i}.png" for i in range(file_count)]

def remove_temp_files(temp_file_names):
    """ Remove a list of temp files """
    for f in temp_file_names:
        os.remove(f)

def save_dyno_gif(write_dir, png_frames, bounce=True, fps=10):
    """
    png_frames = list of strings of png files (from make_temp_file_names)
    bounce = True: gif bounces frames False: gif repeats frames 
    fps = frames per second
    """
    if write_dir[-4:] != ".gif":
        raise ValueError("Save gif dir doesnt end with '.gif'")

    # Make gif file names
    gif_file_names = list.copy(png_frames)
    if bounce:
        gif_file_names.extend(reversed(gif_file_names))

    # Write gif
    imageio.mimsave(write_dir, [imageio.imread(f) for f in gif_file_names], fps=fps)
