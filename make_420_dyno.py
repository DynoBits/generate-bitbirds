## Make 420 dyno
"""
Run this script to create the special edition 420 Dyno 
A gif named 420_dyno.gif will appear in the current directory
"""

# library to interact with the operating system
import os

from dyno_bit import DynoBit
import dyno_colors as dc
from make_smoking_dyno import make_smoking_dyno

"""
emotion="Happy"
species="Euoplorex"
activity="Diurnal"
background_color=dc.LIGHT_WHITE
outline_color=dc.BLACK
eyebrow_color=dc.BLACK
limbs_color=dc.BLACK
sclera_color=dc.WHITE
pupil_color=dc.BLACK
skin_color=dc.GRASS
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

spot1_out_color = dc.lighter(spot1_in_color)
spot2_out_color = dc.lighter(spot2_in_color)
spot3_out_color = dc.lighter(spot3_in_color)
spot4_out_color = dc.lighter(spot4_in_color)
spot5_out_color = dc.lighter(spot5_in_color)

emotion="Happy",
species="Euoplorex",
activity="Diurnal",
background_color=dc.LIGHT_WHITE,
outline_color=dc.BLACK,
eyebrow_color=dc.BLACK,
limbs_color=dc.BLACK,
sclera_color=dc.WHITE,
pupil_color=dc.BLACK,
skin_color=dc.GRASS,
horn_color=(0,75,0),
"""
tail_color=(0,255,0)
spike_color_list=[(0,118,0),(0,165,0),(0,205,0),(0,238,0)]
spot_in_color_list=[tail_color,spike_color_list[3],spike_color_list[2],spike_color_list[1],spike_color_list[0]]
spot_out_color_list=[dc.lighter(spot_in_color_list[0]),dc.lighter(spot_in_color_list[1]),dc.lighter(spot_in_color_list[2]),dc.lighter(spot_in_color_list[3]),dc.lighter(spot_in_color_list[4])]

dyno_420 = DynoBit(
        emotion="Happy",
        species="Euoplorex",
        activity="Diurnal",
        background_color=dc.LIGHT_WHITE,
        outline_color=dc.BLACK,
        eyebrow_color=dc.BLACK,
        limbs_color=dc.BLACK,
        sclera_color=dc.WHITE,
        pupil_color=dc.BLACK,
        skin_color=dc.GRASS,
        horn_color=(0,75,0),
        tail_color=tail_color,
        spike_color_list=spike_color_list,
        spot_in_color_list=spot_in_color_list,
        spot_out_color_list=spot_out_color_list
    )

# 420 dyno
make_smoking_dyno(f"{os.getcwd()}/420_dyno.gif", dyno_420)
