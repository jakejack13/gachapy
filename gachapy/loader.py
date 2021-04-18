"""Collection of loader functions for loading gachapy objects from json files. 
These functions can be used to save and load Controller objects to and from
json files. This should be used to save and load game state of active 
gachapy games.

These functions operate as the Loader of a gachapy game

Author: Jacob Kerr, 2021
"""

from gachapy.objects import *
from gachapy.controller import *
import json


def load_controller(
    items_filename: str, banners_filename: str, players_filename: str
) -> Controller:
    """Creates a Controller object from the specified json files

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
    _load_items_from_file(items_filename, controller)
    _load_banners_from_file(banners_filename, controller)
    _load_players_from_file(players_filename, controller)
    return controller


def save_controller(
    controller: Controller,
    items_filename: str,
    banners_filename: str,
    players_filename: str,
) -> None:
    """Saves the controller in json format into the specified files

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
    _save_items_to_file(items_filename, controller)
    _save_banners_to_file(banners_filename, controller)
    _save_players_to_file(players_filename, controller)


def _load_items_from_file(
    filename: str, controller: Controller
) -> List[Optional[Item]]:
    """Load items into controller from the specified json file

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
    try:
        with open(filename) as f:
            j = json.load(f)
            items_str_list = j["items"]
            return [
                controller.add_new_item(i["name"], i["id"], i["rarity"])
                for i in items_str_list
            ]
    except:
        return []


def _load_banners_from_file(
    filename: str, controller: Controller
) -> List[Optional[Banner]]:
    """Load banners into controller from the specified json file

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
    try:
        with open(filename) as f:
            j = json.load(f)
            banner_str_list = j["banners"]
            return [
                controller.add_new_banner(
                    i["name"], i["id"], [j["id"] for j in i["items"]], i["price"]
                )
                for i in banner_str_list
            ]
    except:
        return []


def _load_players_from_file(
    filename: str, controller: Controller
) -> List[Optional[Player]]:
    """Load players into controller from the specified json file

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
    try:
        with open(filename) as f:
            j = json.load(f)
            player_str_list = j["players"]
            return [
                controller.add_new_player(
                    i["name"], i["id"], i["money"], [j["id"] for j in i["items"]]
                )
                for i in player_str_list
            ]
    except:
        return []


def _save_items_to_file(filename: str, controller: Controller) -> None:
    """Save items from controller into the specified json file

    Parameters
    ----------
    filename : str
        the path of the json file to save
    controller : Controller
        the controller to load the items from

    Returns
    -------
    None
    """
    items_list = controller.items.values()
    item_dict = {
        "items": [{"name": i.name, "id": i.id, "rarity": i.rarity} for i in items_list]
    }
    with open(filename, "w") as f:
        json.dump(item_dict, f)


def _save_banners_to_file(filename: str, controller: Controller) -> None:
    """Save banners from controller into the specified json file

    Parameters
    ----------
    filename : str
        the path of the json file to save
    controller : Controller
        the controller to load the banners from

    Returns
    -------
    None
    """
    banners_list = controller.banners.values()
    banner_dict = {
        "banners": [
            {
                "name": i.name,
                "id": i.id,
                "items": [{"id": j.id} for j in i.item_list],
                "price": i.price,
            }
            for i in banners_list
        ]
    }
    with open(filename, "w") as f:
        json.dump(banner_dict, f)


def _save_players_to_file(filename: str, controller: Controller) -> None:
    """Save players from controller into the specified json file

    Parameters
    ----------
    filename : str
        the path of the json file to save
    controller : Controller
        the controller to load the players from

    Returns
    -------
    None
    """
    players_list = controller.players.values()
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
    with open(filename, "w") as f:
        json.dump(player_dict, f)