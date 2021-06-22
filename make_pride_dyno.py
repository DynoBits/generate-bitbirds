## Make 420 dyno
"""
Run this script to create the special edition pride DynoBit 669
A gif named pride_dyno.gif will appear in the current directory
"""

# library to interact with the operating system
import os

from dyno_bit import DynoBit
import dyno_colors as dc
from make_disco_dyno import make_disco_dyno

horn_color=dc.RED
tail_color=dc.INDIGO
spike_color_list=[dc.ORANGE,dc.YELLOW,dc.GREEN,dc.BLUE]
spot_in_color_list=[spike_color_list[0],spike_color_list[1],spike_color_list[2],spike_color_list[3],tail_color]
spot_out_color_list=[dc.lighter(spot_in_color_list[0]),dc.lighter(spot_in_color_list[1]),dc.lighter(spot_in_color_list[2]),dc.lighter(spot_in_color_list[3]),dc.lighter(spot_in_color_list[4])]

pride_dyno = DynoBit(
        emotion="Happy",
        species="Euoplorex",
        activity="Diurnal",
        background_color=dc.LIGHT_WHITE,
        outline_color=dc.BLACK,
        eyebrow_color=dc.BLACK,
        limbs_color=dc.BLACK,
        sclera_color=dc.WHITE,
        pupil_color=dc.BLACK,
        skin_color=dc.VIOLET,
        horn_color=horn_color,
        tail_color=tail_color,
        spike_color_list=spike_color_list,
        spot_in_color_list=spot_in_color_list,
        spot_out_color_list=spot_out_color_list
    )

# Pride dyno
make_disco_dyno(f"{os.getcwd()}/pride_dyno.gif", pride_dyno)
