import dyno_colors as dc
from dyno_bit import DynoBit
from dyno_gif import make_temp_file_names, remove_temp_files, save_dyno_gif


def make_disco_dyno(gif_name, dyno=DynoBit(), disco_attr_name="background_color", disco_color_list=dc.RAINBOW): 
    temp_file_names = make_temp_file_names(len(disco_color_list), "temp_disco")
    
    for i in range(len(disco_color_list)):
        setattr(dyno, disco_attr_name, disco_color_list[i])
        dyno.save_dyno_image(imgname=temp_file_names[i])

    save_dyno_gif(gif_name, temp_file_names, bounce=False)

    remove_temp_files(temp_file_names)
