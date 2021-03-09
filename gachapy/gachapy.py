"""The entry point into the gachapy library

Functions
load_controller(items_filename,banners_filename,players_filename) : Controller
    Creates a Controller object from the specified json files
save_controller(controller,items_filename,banners_filename,players_filename) : None
    Saves the controller in json format into the specified files
"""

from gachapy.objects import *
from gachapy.controller import *
from gachapy.loader import *

def load_controller(items_filename,banners_filename,players_filename) -> Controller :
    """Creates a Controller object from the specified json files

    Parameters
    items_filename : str
        the path of the items json file
    banners_filename : str
        the path of the banners json file
    players_filename : str
        the path of the players json file
    
    Returns
    Controller
        the controller loaded from the specified files
    """
    controller = Controller()
    load_items_from_file(items_filename,controller)
    load_banners_from_file(banners_filename,controller)
    load_players_from_file(players_filename,controller)
    return controller

def save_controller(controller,items_filename,banners_filename,players_filename) -> None :
    """Saves the controller in json format into the specified files

    Parameters
    controller : Controller 
        the controller to save into files
    items_filename : str
        the path of the items json file
    banners_filename : str
        the path of the banners json file
    players_filename : str
        the path of the players json file

    Return
    None
    """
    items_list = controller.items
    item_dict = {"items": [{"name":i.name,"description":i.description,"rarity":i.rarity} for i in items_list]}
    with open(items_filename, "w") as f:
        json.dump(item_dict,f)
    banners_list = controller.banners
    banner_dict = {"banners": [{"name":i.name,"items":[{"name":j.name} for j in i.item_list],"modifier":i.modifier,"price":i.price}] for i in banners_list}
    with open(banners_filename, "w") as f:
        json.dump(banner_dict,f)
    players_list = controller.players
    player_dict = {"players": [{"name":i.name,"money":i.money,"items":[{"name":j.name} for j in i.items]} for i in players_list]}
    with open(players_filename, "w") as f:
        json.dump(player_dict,f)