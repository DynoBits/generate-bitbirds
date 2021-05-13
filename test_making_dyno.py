"""
This script is used to test each power function
To use, make sure a folder named 'test_dyno_gifs' is in current dir and empty
Next, cd to this dir and run this command in console of choice:
	python test_making_dyno.py
If there are no errors and 7 .gif files are made and look good, youre ready to start making powerful dynos!
"""

# library to interact with the operating system
import os

import copy

from dyno_bit import DynoBit


from make_laser_dyno import make_laser_dyno
from make_disco_dyno import make_disco_dyno
from make_eye_roll_dyno import make_eye_roll_dyno 
from make_glowing_dyno import make_glowing_dyno
from make_evolving_dyno import make_evolving_dyno
from make_smoking_dyno import make_smoking_dyno
from make_static_dyno import make_static_dyno


TEST_DYNO_BASE = DynoBit()

TEST_DYNO = copy.copy(TEST_DYNO_BASE)
TEST_DYNO.randomize()
make_laser_dyno(f"{os.getcwd()}/test_dyno_gifs/test_laser_dyno.gif", TEST_DYNO)

TEST_DYNO = copy.copy(TEST_DYNO_BASE)
TEST_DYNO.randomize()
make_disco_dyno(f"{os.getcwd()}/test_dyno_gifs/test_disco_dyno.gif", TEST_DYNO)

TEST_DYNO = copy.copy(TEST_DYNO_BASE)
TEST_DYNO.randomize()
make_eye_roll_dyno(f"{os.getcwd()}/test_dyno_gifs/test_eye_roll_dyno.gif", TEST_DYNO)

TEST_DYNO = copy.copy(TEST_DYNO_BASE)
TEST_DYNO.randomize()
make_glowing_dyno(f"{os.getcwd()}/test_dyno_gifs/test_glowing_dyno.gif", TEST_DYNO)

TEST_DYNO = copy.copy(TEST_DYNO_BASE)
TEST_DYNO.randomize()
make_evolving_dyno(f"{os.getcwd()}/test_dyno_gifs/test_evolving_dyno.gif", TEST_DYNO)

TEST_DYNO = copy.copy(TEST_DYNO_BASE)
TEST_DYNO.randomize()
make_smoking_dyno(f"{os.getcwd()}/test_dyno_gifs/test_smoking_dyno.gif", TEST_DYNO)

TEST_DYNO = copy.copy(TEST_DYNO_BASE)
TEST_DYNO.randomize()
make_static_dyno(f"{os.getcwd()}/test_dyno_gifs/test_static_dyno.gif", TEST_DYNO)
