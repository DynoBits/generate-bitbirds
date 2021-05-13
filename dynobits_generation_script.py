"""
This script was used to create all generated DynoBit NFTs on OpenSea (000-799 excluding special editions)

Ensure you can successfully run test_making_dyno.py before using this script

To make dynos, make sure a folder named 'dyno_images' & 'dyno_gifs' is in current dir and empty
Next, cd to this dir and run this command in console of choice:
    python dynobits_generation_script.py
The default script will create 400 dyno images in /dyno_images and 400 dyno gifs in /dyno_gifs
It should take about 5 minutes to generate these Dynos
"""

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

from dyno_bit import DynoBit
import dyno_colors as dc

# Dyno Gif functions - see .py of each function for code
from make_laser_dyno import make_laser_dyno
from make_disco_dyno import make_disco_dyno
from make_eye_roll_dyno import make_eye_roll_dyno 
from make_glowing_dyno import make_glowing_dyno
from make_evolving_dyno import make_evolving_dyno
from make_smoking_dyno import make_smoking_dyno
from make_static_dyno import make_static_dyno


# Get current working directory - used to write images to
cwd = os.getcwd()

# COUNTS FOR TRACKING RESULTS
count_al_color = [0, 0, 0, 0, 0] # Grey, Gold, Red, White, Black
count_dyno_type = [0, 0, 0] # Euoplocephalus, T-Tex, Euoplorex
count_emotion = [0, 0, 0] # mad, happy, neutral
count_nocturnal = 0
count_eye_mutation = 0
count_mismatch_spikes = 0
count_mismatch_dots = 0

number_of_power = 0
count_power = [0, 0, 0, 0, 0, 0, 0] # evolving, smoking, glowing, disco, laser, eye roll, static


def feed_dyno():
    '''Progress seed by random int - the more you feed your dyno, the more random it becomes'''
    n = randint(0, 999)
    seed(n)
    return n


def random_color():
    '''generates random color rgb between (0, 0, 0) and (255, 255, 255) inclusive'''
    feed_dyno()
    return dc.random_color()


save_dyno = True # Set to false to skip writing the dyno image - used to debug quickly - note: will change randomness of gifs if False
print_attributes = False # Set to true to print the attributes of each dyno after creation
dyno_count = 800 # number of dynos to create - 800 used for OpenSea NFTs DynoBit 000-799 (excluding special editions)
for dyno_number in range(dyno_count):

    is_nocturnal = feed_dyno() % 2 # 50% chance dyno is nocturnal (night-mode)
    has_eye_mutation = feed_dyno() < 100 # 10% chance of eye mutation
    has_mismatch_spikes = feed_dyno() < 150 # 15% chance of mismatch spikes
    has_mismatch_dots = feed_dyno() < 150 # 15% chance of mismatch dots

    # using ETH block number as starting random number seed
    b = 11981207
    seed(b + dyno_number)

    # Background color
    bg = (238, 238, 238)

    # Outline color
    ol = (0, 0, 0)

    if is_nocturnal: 
        bg,ol = ol,bg
        count_nocturnal += 1
        activity = "Nocturnal"
    else:
        activity = "Diurnal"

    # Eyebrow
    eb = (0, 0, 0)

    # Skin color
    sk = random_color()

    # Horn color
    hn = random_color()

    '''----- ARMS & LEGS -----'''
    al_type = feed_dyno()

    if al_type > 500:
        # 50% chance of grey arms and legs
        al = (152, 152, 152)
        count_al_color[0] += 1
        arms_and_legs = "Grey"
    elif al_type > 50:
        # 45% chance of gold arms and legs
        al = (204, 172, 0)
        count_al_color[1] += 1
        arms_and_legs = "Gold"
    elif al_type > 10:
        # 4% chance of red arms and legs
        al = (204, 0, 0)
        count_al_color[2] += 1
        arms_and_legs = "Red"
    else:
        # 1% chance of black/white arms and legs
        al = ol
        if is_nocturnal: # White arms if nocturnal
            count_al_color[3] += 1
            arms_and_legs = "White"
        else: # Black arms if diurnal
            count_al_color[4] += 1
            arms_and_legs = "Black"
    
    '''----- EYES -----'''
    if has_eye_mutation:
        sc = random_color() # Sclera color - the "white" part of eye
        pu = (154, 0, 0) # Pupil color - the black part of eye
        eye = "Mutation"
        count_eye_mutation += 1
    else: 
        sc = (240,248,255)
        pu = (0, 0, 0)
        eye = "Normal"

    '''----- SPIKES & TAIL -----'''
    if has_mismatch_spikes: # 4 total spikes & 1 tail
        s1 = random_color()
        s2 = random_color()
        s3 = random_color()
        s4 = random_color()
        tl = random_color()
    else: 
        s1 = s2 = s3 = s4 = tl = random_color()

    '''----- DOTS -----'''
    if has_mismatch_dots: # 5 total with inner and outer
        i1 = random_color()
        o1 = dc.lighter(i1)
        i2 = random_color()
        o2 = dc.lighter(i2)
        i3 = random_color()
        o3 = dc.lighter(i3)
        i4 = random_color()
        o4 = dc.lighter(i4)
        i5 = random_color()
        o5 = dc.lighter(i5)
    else: 
        i1 = i2 = i3 = i4 = i5 = random_color()
        o1 = o2 = o3 = o4 = o5 = dc.lighter(i1)

    '''----- Dyno type -----'''
    spikes_and_tail = "None"
    spots = "None"
    dyno_type = feed_dyno()

    if dyno_type > 444: # 55.5% chance of Euoplocephalus
        count_dyno_type[0] += 1
        species = "Euoplocephalus"
        if has_mismatch_spikes: 
            count_mismatch_spikes += 1
            spikes_and_tail = "Mismatch"
        else:
            spikes_and_tail = "Match"
    elif dyno_type > 111: # 33.3% chance of T-Tex
        count_dyno_type[1] += 1
        species = "T-Rex"
        if has_mismatch_dots: 
            count_mismatch_dots += 1
            spots = "Mismatch"
        else:
            spots = "Match"
    else: # 11.1 % chance of Euoplorex - A cross breed of Euoplocephalus & T-Tex
        count_dyno_type[2] += 1
        species = "Euoplorex"
        if has_mismatch_spikes: 
            count_mismatch_spikes += 1
            spikes_and_tail = "Mismatch"
        else:
            spikes_and_tail = "Match"
        if has_mismatch_dots: 
            count_mismatch_dots += 1
            spots = "Mismatch"
        else:
            spots = "Match"


    '''----- Emotion -----'''
    emotion = feed_dyno() % 3 # 33% chance of each emotion

    if emotion == 0: # 33% chance of mad eyebrows
        emtn = "Angry"
    elif emotion == 1: # 33% chance of happy eyebrows
        emtn = "Happy"
    else: # 33% chance of neutral eyebrows
        emtn = "Neutral"

    count_emotion[emotion] += 1

    # Make dyno with randomly generated attributes 
    dyno = DynoBit(
            emotion=emtn,
            species=species,
            activity=activity,
            background_color=bg,
            outline_color=ol,
            eyebrow_color=eb,
            limbs_color=al,
            sclera_color=sc,
            pupil_color=pu,
            skin_color=sk,
            horn_color=hn,
            tail_color=tl,
            spike_color_list=[s1,s2,s3,s4],
            spot_in_color_list=[i1,i2,i3,i4,i5],
            spot_out_color_list=[o1,o2,o3,o4,o5]
        )

    # Write dynobit image - First half of dynos are Images, second half are gifs
    if dyno_number < dyno_count/2: # Image
        dyno_image_name = f"{cwd}/dyno_images/{dyno_number}.png"
        if save_dyno: dyno.save_dyno_image(imgname=dyno_image_name)
        power = "None"
    else: # Gif 
        number_of_power += 1
        dyno_gif_name = f"{cwd}/dyno_gifs/{dyno_number}.gif"
        dyno_power = randint(0, 6)
        count_power[dyno_power] += 1
        if dyno_power == 0:
            if save_dyno: make_evolving_dyno(dyno_gif_name, dyno)
            power = "Evolving"
        if dyno_power == 1:
            if save_dyno: make_smoking_dyno(dyno_gif_name, dyno)
            power = "Smoking"
        if dyno_power == 2:
            if save_dyno: make_glowing_dyno(dyno_gif_name, dyno)
            power = "Glowing"
        if dyno_power == 3:
            if save_dyno: make_disco_dyno(dyno_gif_name, dyno)
            power = "Disco"
        if dyno_power == 4:
            if save_dyno: make_laser_dyno(dyno_gif_name, dyno)
            power = "Laser"
        if dyno_power == 5:
            if save_dyno: make_eye_roll_dyno(dyno_gif_name, dyno)
            power = "Eye Roll"
        if dyno_power == 6:
            make_static_dyno(dyno_gif_name, dyno, save_dyno=save_dyno) # save_dyno passed for debugging
            power = "Static"

    if print_attributes:
        print("DynoBit", dyno_number)
        print(f"\tSpecies={species}")
        print(f"\tArms & Legs={arms_and_legs}")
        print(f"\tEmotion={emtn}")
        print(f"\tActivity={activity}")
        print(f"\tEye={eye}")
        print(f"\tSpikes & Tail={spikes_and_tail}")
        print(f"\tSpots={spots}")
        print(f"\tPower={power}\n")


'''
Print out the results of the dyno creation
Displays counts and percentages of each dyno attribute to console
'''
print("-------------------------- DYNO RESULTS --------------------------")

print(f"\nARAMS & LEGS" + 
    f"\n\tGrey({count_al_color[0]}): {round( count_al_color[0]/dyno_count*100 )} %" + 
    f"\n\tGold({count_al_color[1]}): {round( count_al_color[1]/dyno_count*100 )} %" + 
    f"\n\tRed({count_al_color[2]}): {round( count_al_color[2]/dyno_count*100 )} %" + 
    f"\n\tWhite({count_al_color[3]}): {round( count_al_color[3]/dyno_count*100 )} %" + 
    f"\n\tBlack({count_al_color[4]}): {round( count_al_color[4]/dyno_count*100 )} %"
    )

print(f"\nDYNO TYPE" + 
    f"\n\tEuoplocephalus({count_dyno_type[0]}): {round( count_dyno_type[0]/dyno_count*100 )} %" + 
    f"\n\tT-Tex({count_dyno_type[1]}): {round( count_dyno_type[1]/dyno_count*100 )} %" + 
    f"\n\tEuoplorex({count_dyno_type[2]}): {round( count_dyno_type[2]/dyno_count*100 )} %"
    )

print(f"\nEYEBROW TYPE" + 
    f"\n\tMad({count_emotion[0]}): {round( count_emotion[0]/dyno_count*100 )} %" + 
    f"\n\tHappy({count_emotion[1]}): {round( count_emotion[1]/dyno_count*100 )} %" + 
    f"\n\tNeutral({count_emotion[2]}): {round( count_emotion[2]/dyno_count*100 )} %"
    )

print(f"\nNOCTURNAL({count_nocturnal}): {round( count_nocturnal/dyno_count*100 )} %")

print(f"\nEYE MUTATION({count_eye_mutation}): {round( count_eye_mutation/dyno_count*100 )} %")

print(f"\nMISMATCH SPIKES({count_mismatch_spikes}): {round( count_mismatch_spikes/dyno_count*100 )} %")

print(f"\nMISMATCH DOTS({count_mismatch_dots}): {round( count_mismatch_dots/dyno_count*100 )} %")

if number_of_power > 0:
    print(f"\nPOWER TYPE" + 
        f"\n\tEvolving({count_power[0]}): {round( count_power[0]/number_of_power*100 )} %" + 
        f"\n\tSmoking({count_power[1]}): {round( count_power[1]/number_of_power*100 )} %" + 
        f"\n\tGlowing({count_power[2]}): {round( count_power[2]/number_of_power*100 )} %" + 
        f"\n\tDisco({count_power[3]}): {round( count_power[3]/number_of_power*100 )} %" + 
        f"\n\tLaser({count_power[4]}): {round( count_power[4]/number_of_power*100 )} %" + 
        f"\n\tEye Roll({count_power[5]}): {round( count_power[5]/number_of_power*100 )} %" + 
        f"\n\tStatic({count_power[6]}): {round( count_power[6]/number_of_power*100 )} %"
        )