import dyno_colors as dc
from dyno_bit import DynoBit
from dyno_gif import make_temp_file_names, remove_temp_files, save_dyno_gif


def make_glowing_dyno(gif_name, dyno=DynoBit(), glowing_attr_name="skin_color"):
    temp_file_names = make_temp_file_names(10, "temp_glowing")

    # Save middle frame and color
    base_color = getattr(dyno, glowing_attr_name)
    dyno.save_dyno_image(imgname=temp_file_names[5])

    # Save lighter frames
    lighter_color = base_color
    for i in [4, 3, 2, 1, 0]:
        lighter_color = dc.lighter(lighter_color)
        setattr(dyno, glowing_attr_name, lighter_color)
        dyno.save_dyno_image(imgname=temp_file_names[i])

    # Save darker frames
    darker_color = base_color
    for i in [6, 7, 8, 9]:
        darker_color = dc.darker(darker_color)
        setattr(dyno, glowing_attr_name, darker_color)
        dyno.save_dyno_image(imgname=temp_file_names[i])

    save_dyno_gif(gif_name, temp_file_names, bounce=True)

    remove_temp_files(temp_file_names)
