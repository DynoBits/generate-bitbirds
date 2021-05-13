import dyno_colors as dc
from dyno_bit import DynoBit
from dyno_gif import make_temp_file_names, remove_temp_files, save_dyno_gif

# For random list choice 
from random import choice


# Set save_dyno to false if random needed - debugging gif generation script
def make_static_dyno(gif_name, dyno=DynoBit(), static_color_list=None, save_dyno=True):
    frame_count = 10
    temp_file_names = make_temp_file_names(frame_count, "temp_static")
    background_color_index_list = dyno.get_background_index_list()
    dyno_pixels = dyno.pixels()

    # Change backgroud color based on activity if not supplied
    if static_color_list == None:
    	if dyno.activity == "Diurnal":
    		static_color_list = dc.COLOR_LIST_LIGHT_GREYS
    	if dyno.activity == "Nocturnal":
    		static_color_list = dc.COLOR_LIST_DARK_GREYS

    # Apply power and write temp dyno images
    for file in temp_file_names:
        for i in background_color_index_list:
            dyno_pixels[i] = choice(static_color_list)

        dyno.save_dyno_image(dyno_pixels, file)

    if save_dyno:
        save_dyno_gif(gif_name, temp_file_names, bounce=False, fps=25)

    remove_temp_files(temp_file_names)
