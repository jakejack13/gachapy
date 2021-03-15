"""Collection of loader functions for loading gachapy objects from json files
These functions can be used to save and load Controller objects to and from
json files. This should be used to save and load game state of active 
gachapy games.
WARNING: Only use load_controller and save_controller as your top-level loader 
functions. Using the other three helper functions seperately will result in an 
incomplete and uncoupled Controller. Only use if you know what you're doing

These functions operate as the Loader of a gachapy game

Functions
---------
load_controller(items_filename,banners_filename,players_filename) : Controller
    Creates a Controller object from the specified json files
save_controller(controller,items_filename,banners_filename,players_filename) : None
    Saves the controller in json format into the specified files
load_items_from_file(filename,controller) : List[Optional[Item]]
    Load items into controller from the specified json file
load_banners_from_file(filename,controller) : List[Optional[Banner]]
    Load banners into controller from the specified json file
load_players_from_file(filename,controller) : List[Optional[Player]]
    Load players into controller from the specified json file
"""

from gachapy.objects import *
from gachapy.controller import *
import json


def load_controller(items_filename, banners_filename, players_filename) -> Controller:
    """Creates a Controller object from the specified json files
    TOP LEVEL FUNCTION

    Parameters
    ----------
    items_filename : str
        the path of the items json file
    banners_filename : str
        the path of the banners json file
    players_filename : str
        the path of the players json file

    Returns
    -------
    Controller
        the controller loaded from the specified files
    """
    controller = Controller()
    load_items_from_file(items_filename, controller)
    load_banners_from_file(banners_filename, controller)
    load_players_from_file(players_filename, controller)
    return controller


def save_controller(
    controller, items_filename, banners_filename, players_filename
) -> None:
    """Saves the controller in json format into the specified files
    TOP LEVEL FUNCTION

    Parameters
    ----------
    controller : Controller
        the controller to save into files
    items_filename : str
        the path of the items json file
    banners_filename : str
        the path of the banners json file
    players_filename : str
        the path of the players json file

    Returns
    -------
    None
    """
    items_list = controller.items
    item_dict = {
        "items": [{"name": i.name, "id": i.id, "rarity": i.rarity} for i in items_list]
    }
    with open(items_filename, "w") as f:
        json.dump(item_dict, f)
    banners_list = controller.banners
    banner_dict = {
        "banners": [
            {
                "name": i.name,
                "items": [{"id": j.id} for j in i.item_list],
                "price": i.price,
            }
            for i in banners_list
        ]
    }
    with open(banners_filename, "w") as f:
        json.dump(banner_dict, f)
    players_list = controller.players
    player_dict = {
        "players": [
            {
                "name": i.name,
                "id": i.id,
                "money": i.money,
                "items": [{"id": j.id} for j in i.items],
            }
            for i in players_list
        ]
    }
    with open(players_filename, "w") as f:
        json.dump(player_dict, f)


def load_items_from_file(filename, controller) -> List[Optional[Item]]:
    """Load items into controller from the specified json file
    DO NOT USE ALONE (unless you know what you're doing)

    Parameters
    ----------
    filename : str
        the path of the json file to load
    controller : Controller
        the controller to load the items into

    Returns
    -------
    List[Optional[Item]]
        the list of items loaded, elements are None if they already exist in controller
    """
    with open(filename) as f:
        j = json.load(f)
        items_str_list = j["items"]
        return [
            controller.add_new_item(i["name"], i["id"], i["rarity"])
            for i in items_str_list
        ]


def load_banners_from_file(filename, controller) -> List[Optional[Banner]]:
    """Load banners into controller from the specified json file
    DO NOT USE ALONE (unless you know what you're doing)

    Parameters
    ----------
    filename : str
        the path of the json file to load
    controller : Controller
        the controller to load the banners into

    Returns
    -------
    List[Optional[Banner]]
        the list of banners loaded, elements are None if they already exist in controller
    """
    with open(filename) as f:
        j = json.load(f)
        banner_str_list = j["banners"]
        return [
            controller.add_new_banner(
                i["name"], [j["id"] for j in i["items"]], i["price"]
            )
            for i in banner_str_list
        ]


def load_players_from_file(filename, controller) -> List[Optional[Player]]:
    """Load players into controller from the specified json file
    DO NOT USE ALONE (unless you know what you're doing)

    Parameters
    ----------
    filename : str
        the path of the json file to load
    controller : Controller
        the controller to load the players into

    Returns
    -------
    List[Optional[Player]]
        the list of players loaded, elements are None if they already exist in controller
    """
    with open(filename) as f:
        j = json.load(f)
        player_str_list = j["players"]
        return [
            controller.add_new_player(
                i["name"], i["id"], i["money"], [j["id"] for j in i["items"]]
            )
            for i in player_str_list
        ]
