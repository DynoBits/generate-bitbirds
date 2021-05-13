import dyno_colors as dc
from dyno_bit import DynoBit
from dyno_gif import make_temp_file_names, remove_temp_files, save_dyno_gif

import copy


def make_smoking_dyno(gif_name, dyno=DynoBit()):
    frame_count = 10
    temp_file_names = make_temp_file_names(frame_count, "temp_smoking")
    base_pixels = dyno.pixels()

    # Bloodshot eyes
    base_pixels[[6, 6, 7], [17, 16, 16]] = dc.BLOOD
    base_pixels[7, 17] = dc.BLACK

    # Blunt
    curr_frame = 0
    base_pixels[12, [20, 21, 22]] = dc.BRICK 
    base_pixels[12, 22] = dc.RED
    dyno.save_dyno_image(pixel_array=base_pixels, imgname=temp_file_names[curr_frame])

    # Smoke
    curr_frame = 1
    working_dyno = copy.copy(base_pixels)
    working_dyno[12, 22] = dc.darker(dc.RED, 0.1)
    working_dyno[11, 22] = dc.SMOKE
    dyno.save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 2
    working_dyno = copy.copy(base_pixels)
    working_dyno[12, 22] = dc.darker(dc.RED, 0.1)
    working_dyno[[11, 10], [22, 22]] = dc.SMOKE
    dyno.save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 3
    working_dyno = copy.copy(base_pixels)
    working_dyno[[11, 10, 9], [22, 22, 21]] = dc.SMOKE
    dyno.save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 4
    working_dyno = copy.copy(base_pixels)
    working_dyno[[11, 10, 8, 9], [22, 22, 21, 22]] = dc.SMOKE
    dyno.save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 5
    working_dyno = copy.copy(base_pixels)
    working_dyno[12, 22] = dc.darker(dc.RED, 0.1)
    working_dyno[[11, 10, 7, 8, 9], [22, 22, 21, 22, 21]] = dc.SMOKE
    dyno.save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 6
    working_dyno = copy.copy(base_pixels)
    working_dyno[12, 22] = dc.darker(dc.RED, 0.1)
    working_dyno[[11, 10, 6, 7, 8, 9], [22, 22, 20, 22, 21, 22]] = dc.SMOKE
    dyno.save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 7
    working_dyno = copy.copy(base_pixels)
    working_dyno[[11, 10, 5, 6, 7, 8, 9], [22, 22, 20, 21, 21, 22, 21]] = dc.SMOKE
    dyno.save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 8
    working_dyno = copy.copy(base_pixels)
    working_dyno[[11, 10, 4, 5, 6, 5, 7, 8, 9], [22, 22, 19, 20, 21, 22, 22, 21, 22]] = dc.SMOKE
    dyno.save_dyno_image(working_dyno, temp_file_names[curr_frame])

    curr_frame = 9
    working_dyno = copy.copy(base_pixels)
    working_dyno[12, 22] = dc.darker(dc.RED, 0.1)
    working_dyno[[11, 10, 3, 4, 5, 4, 6, 7, 8, 9], [22, 22, 19, 19, 20, 22, 21, 21, 22, 21]] = dc.SMOKE
    dyno.save_dyno_image(working_dyno, temp_file_names[curr_frame])

    save_dyno_gif(gif_name, [temp_file_names[0]]+temp_file_names, bounce=False, fps=5)

    remove_temp_files(temp_file_names)



# Tests
"""
make_smoking_dyno('/Users/zachgoodenow/Desktop/generate-dynobits/src/test_smoking.gif')

test_dyno = DynoBit()
test_dyno.randomize()
make_smoking_dyno('/Users/zachgoodenow/Desktop/generate-dynobits/src/test_smoking.gif', test_dyno)


make_smoking_dyno(f"{os.getcwd()}/aaa_test_smoking_e.png", make_dyno_image(species="Euoplocephalus"))
make_smoking_dyno(f"{os.getcwd()}/aaa_test_smoking_t.png", make_dyno_image(species="T-Rex"))
make_smoking_dyno(f"{os.getcwd()}/aaa_test_smoking_x.png", make_dyno_image(species="Euoplorex"))
"""
