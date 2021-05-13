import dyno_colors as dc
from dyno_bit import DynoBit
from dyno_gif import make_temp_file_names, remove_temp_files, save_dyno_gif


def make_laser_dyno(gif_name, dyno=DynoBit(), laser_color=dc.RED):
    laser_index_list = [(7,17), (8,18), (9,19), (10,20), (11,21), (12,22), (13,23)]
    temp_file_names = make_temp_file_names(len(laser_index_list)+1, "temp_laser")
    pixels = dyno.pixels()

    dyno.save_dyno_image(imgname=temp_file_names[0])
    for i in range(len(laser_index_list)):
        pixels[laser_index_list[i]] = laser_color
        dyno.save_dyno_image(pixel_array=pixels, imgname=temp_file_names[i+1])

    save_dyno_gif(gif_name, temp_file_names, bounce=True)

    remove_temp_files(temp_file_names)
