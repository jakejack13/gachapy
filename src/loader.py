"""Collection of loader functions for loading gachapy objects from json files

Functions
load_items_from_file(filename,controller) : List[Optional[Item]]
    Load items into controller from the specified json file
load_banners_from_file(filename,controller) : List[Optional[Banner]]
    Load banners into controller from the specified json file
load_players_from_file(filename,controller) : List[Optional[Player]]
    Load players into controller from the specified json file
"""

from objects import *
from controller import *
import json

def load_items_from_file(filename,controller) -> List[Optional[Item]] :
    """Load items into controller from the specified json file

    Parameters
    filename : str
        the path of the json file to load
    controller : Controller
        the controller to load the items into
    
    Returns
    List[Optional[Item]]
        the list of items loaded, elements are None if they already exist in controller
    """
    with open(filename) as f :
        j = json.load(f)
        items_str_list = j["items"]
        return [controller.add_new_item(i["name"],i["description"],i["rarity"]) for i in items_str_list]

def load_banners_from_file(filename,controller) -> List[Optional[Banner]] :
    """Load banners into controller from the specified json file

    Parameters
    filename : str
        the path of the json file to load
    controller : Controller
        the controller to load the banners into

    Returns
    List[Optional[Banner]]
        the list of banners loaded, elements are None if they already exist in controller
    """
    with open(filename) as f :
        j = json.load(f)
        banner_str_list = j["banners"]
        return [controller.add_new_banner(i["name"],[j["name"] for j in i["items"]],i["modifier"],i["price"]) for i in banner_str_list]

def load_players_from_file(filename,controller) -> List[Optional[Player]] :
    """Load players into controller from the specified json file

    Parameters
    filename : str
        the path of the json file to load
    controller : Controller
        the controller to load the players into

    Returns
    List[Optional[Player]]
        the list of players loaded, elements are None if they already exist in controller
    """
    with open(filename) as f :
        j = json.load(f)
        player_str_list = j["players"]
        return [controller.add_new_player(i["name"],i["money"],[j["name"] for j in i["items"]]) for i in player_str_list]