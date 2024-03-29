gachapy - a Python engine for gacha games
=========================================

What is this?
=============
gachapy is a collection of both low and high level objects that can be used as a framework to create gacha games. It contains a Controller class for high level management of the game, abstracting away the nitty gritty of item and player management. Controllers can be saved and loaded through the loader library of functions to and from JSON formatted files. More information can be found in the documentation below. 

Install through pip
===================
| pip install gachapy

Project Sources
===============
| `GitHub <https://github.com/jakejack13/gachapy>`_
| `PyPi <https://pypi.org/project/gachapy/>`_

Example Application
===================
::

   import gachapy

   # Creating controller
   controller = gachapy.Controller()

   # Add items to game with differing rarities
   controller.add_new_item("apple","a",2)
   controller.add_new_item("banana","b",3)
   controller.add_new_item("carrot","c",10)

   # Create new banner with the items that have already been added and cost of 5
   controller.add_new_banner("food","f",["a","b","c"],5,"1 + 1 / R")

   # Create new player with 100 starting money and no starting items
   controller.add_new_player("jacob","j",100)

   # Player "jacob" pulls from banner "food"
   controller.pull("j","f")

   # Get player "jacob"
   jacob = controller.find_player_by_id("j")

   # Show information about "jacob"
   print(jacob)

   # Save controller into respective files
   gachapy.save_controller(controller,"save.json")


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   modules/gachapy
   modules/gachapy.objects
   modules/gachapy.controller
   modules/gachapy.loader
   modules/gachapy.keylang


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`