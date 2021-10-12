# GachaPy

A gacha engine built in Python for developing gacha games

### What is this?
gachapy is a collection of both low and high level objects that can be used as a framework to create gacha games. It contains a Controller class for high level management of the game, abstracting away the nitty gritty of item and player management. Controllers can be saved and loaded through the loader library of functions to and from JSON formatted files. More information can be found in the documentation below. 

### Features
- A collection of low level objects that makes creating new items, banners, and players simple
- A controller that consolidates all of the game information into a single, simple-to-use object
- Saving and loading of game state using JSON
- A custom made calculator-like language, KeyLang, for saving and loading custom item rarity to drop rate functions
- Automatically updated documentation hosted on ReadTheDocs
- A Docker image on DockerHub that provides the easiest way to start development with gachapy

### Install through pip
```pip install gachapy```

[gachapy PyPi page](https://pypi.org/project/gachapy/)

### Documentation
[gachapy documentation](https://gachapy.readthedocs.io/)

### Example Application
```python
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
```

More examples can be found in the `examples/` directory

### History 
gachapy started out as a joke. I was talking to my roommate at the time about his gacha game addiction and how he spent frankly outrageous amounts of money on them when I started to develop an idea. Why don't I design a gacha Discord bot and profit off of his addiction? Of course, both he and I knew he wouldn't pay a dime to me but the seeds of the idea were already planted. However, just a few minutes into the designing the Discord bot, I decided to make a separate library for all of the gacha-related functions before moving forward with the client. Thus, gachapy was born. I finished designing and implementing the initial framework, just a collection of low level objects and a controller, in a single night (not getting much sleep, admittedly). The next day, I published the package on PyPi, my first Python package ever published. A few days after, I added documentation hosted on ReadTheDocs, also a first for me. Later came unit tests for all modules, a loader and saver, and finally, just recently, KeyLang. gachapy has been in on and off development for a while but I consider it to be my most fully fleshed out piece of software, including unit testing, CI/CD pipelines with Semaphore, Docker images, and package hosting. 