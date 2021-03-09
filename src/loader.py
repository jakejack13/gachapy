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
    f = open(filename)
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
    f = open(filename)
    j = json.load(f)
    banner_str_list = j["banners"]
    return [controller.add_new_banner(i["name"],[j["name"] for j in i["items"]],i["modifier"],i["price"]) for i in banner_str_list]

def load_players_from_file(filename,controller) -> List[Optional[Player]] :
    f = open(filename)
    j = json.load(f)
    player_str_list = j["players"]
    return [controller.add_new_player(i["name"],i["money"],[j["name"] for j in i["items"]]) for i in player_str_list]