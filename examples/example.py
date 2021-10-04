import gachapy

# Creating controller
controller = gachapy.Controller()

# Add items to game with differing rarities
controller.add_new_item("apple","a",2)
controller.add_new_item("banana","b",3)
controller.add_new_item("carrot","c",10)

# Create new banner with the items that have already been added and cost of 5
controller.add_new_banner("food","f",["a","b","c"],5)

# Create new player with 100 starting money and no starting items
controller.add_new_player("jacob","j",100)

# Player "jacob" pulls from banner "food"
controller.pull("j","f")

# Get player "jacob"
jacob = controller.find_player_by_id("j")

# Show information about "jacob"
print(jacob)

# Save controller into respective files
gachapy.save_controller(controller,"items.json","banners.json","players.json")