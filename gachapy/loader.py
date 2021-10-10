"""Library of loader functions for loading gachapy objects from json files. 
These functions can be used to save and load Controller objects to and from
json files. This should be used to save and load game state of active 
gachapy games. Loading and saving objects lower than the Controller (Items, 
Banners, Players) separately is not supported. 

Examples of the structure that gachapy json files should follow can be found
in the examples/ directory

These functions operate as the Loader of a gachapy game

Author: Jacob Kerr, 2021
"""

from .objects import *
from .controller import *
import json


def load_controller(
    filename: str
) -> Controller:
    """Creates a Controller object from the specified json files

    Parameters
    ----------
    filename : str
        the path of the json file

    Returns
    -------
    Controller
        the controller loaded from the specified files
    """
    controller = None
    with open(filename, 'r') as f:
        controller = Controller()
        json_obj = json.load(f)
        
        items = json_obj["items"]
        for item in items:
            controller.add_new_item(
                item["name"],item["id"],float(item["rarity"]))
        
        banners = json_obj["banners"]
        for banner in banners:
            controller.add_new_banner(
                banner["name"],
                banner["id"],
                [item["id"] for item in banner["items"]],
                float(banner["price"]), banner["key"])
        
        players = json_obj["players"]
        for player in players:
            controller.add_new_player(
                player["name"],
                player["id"],
                float(player["money"]),
                [item["id"] for item in player["items"]])
    return controller


def save_controller(
    controller: Controller,
    filename: str
) -> None:
    """Saves the controller in json format into the specified files

    Parameters
    ----------
    controller : Controller
        the controller to save into files
    filename : str
        the path to the json file

    Returns
    -------
    None
    """
    with open(filename, 'w') as f:
        items_list = []
        for item in controller.items.values():
            item_dict = {
                "name":item.name,
                "id":item.id,
                "rarity":item.rarity}
            items_list.append(item_dict)
        
        banners_list = []
        for banner in controller.banners.values():
            banner_dict = {
                "name":banner.name,
                "id":banner.id,
                "items":[{"id":item.id} for item in banner.items],
                "price":banner.price,
                "key":banner.key}
            banners_list.append(banner_dict)
        
        players_list = []
        for player in controller.players.values():
            player_dict = {
                "name":player.name,
                "id":player.id,
                "money":player.money,
                "items":[{"id":item.id} for item in player.items]}
            players_list.append(player_dict)

        controller_dict = {
        "items":items_list,"banners":banners_list,"players":players_list}
        json.dump(controller_dict,f)