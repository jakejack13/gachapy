"""A Python engine for gacha games

Directory
---------
controller
    The controller used for all high level management of the gacha game
objects
    Objects used for low level management and data storage of the gacha game
loader
    Library of loader functions for loading gachapy objects from json files

Author: Jacob Kerr, 2021
"""

from .objects import *
from .controller import *
from .loader import *
