"""The controller used for all high level management of the gacha game. 
Instances of this class should be created for each instance of a gacha game 
you would like to run. These instances should then be used to access and 
manage the Item, Banner, and Player objects in the game directly. Once 
accessed, the objects can then be modified directly using class methods (see 
objects.py for more info).

This object operates as the Controller of a gachapy game 

Author: Jacob Kerr, 2021
"""

from typing import Dict, Optional
from gachapy.objects import *


def default_key(rarity: float) -> float:
    """The default function that converts rarity to drop rate (1/x)

    Parameters
    ----------
    rarity : float
        the rarity of the item

    Returns
    -------
    float
        the drop rate of the item
    """
    return 1 / rarity


def _sort_player_key(player: Player) -> int:
    """The key used to sort players in a list of players

    Parameters
    ----------
    player : Player
        the player to extract the key from

    Returns
    -------
    int
        the key of the player
    """
    return sum([i.rarity for i in player.items])


class PullError(Exception):
    """An exception thrown when pulling from a banner"""

    pass


class Controller:
    """A controller used to control an instance of a gacha game. Used to
    perform all actions needed in a game and manage game information in the
    form of gachapy objects

    Fields
    ------
    items : List[Item]
        the list of items that are in the item pool for the gacha
    banners : List[Banner]
        the list of banners that are available for the gacha
    players : List[Player]
        the list of players enrolled in the gacha
    """

    def __init__(
        self,
        items: Dict[str, Item] = {},
        banners: Dict[str, Banner] = {},
        players: Dict[str, Player] = {},
    ) -> None:
        """Creates an instance of a gacha controller

        Parameters
        ----------
        items : Dict[str,Item]
            the dict of id, item pairs that are in the item pool for the gacha
        banners : Dict[str,Banner]
            the dict of id, banner pairs that are available for the gacha
        players : Dict,str[Player]
            the dict of id, player pairs enrolled in the gacha
        """
        self.items = items
        self.banners = banners
        self.players = players

    def find_item_by_name(self, item_name: str) -> Optional[Item]:
        """Returns the Item object with the given name or None if not found
        DEPRICATED: consider using find_item_by_id

        Parameters
        ----------
        item_name : str
            the name of the item

        Returns
        -------
        Optional[Item]
            the item object with the given name or None if not found
        """
        item = [i for i in self.items.values() if i.name == item_name]
        if len(item) < 1:
            return None
        return item[0]

    def find_banner_by_name(self, banner_name: str) -> Optional[Banner]:
        """Returns the Banner object with the given name or None if not found
        DEPRICATED: consider using find_banner_by_id

        Parameters
        ----------
        banner_name : str
            the name of the banner

        Returns
        -------
        Optional[Banner]
            the banner object with the given name or None if not found
        """
        banner = [i for i in self.banners.values() if i.name == banner_name]
        if len(banner) < 1:
            return None
        return banner[0]

    def find_player_by_name(self, player_name: str) -> Optional[Player]:
        """Returns the Player object with the given name or None if not found
        DEPRICATED: consider using find_player_by_id

        Parameters
        ----------
        player_name : str
            the name of the player

        Returns
        -------
        Optional[player]
            the player object with the given name or None if not found
        """
        player = [i for i in self.players.values() if i.name == player_name]
        if len(player) < 1:
            return None
        return player[0]

    def find_item_by_id(self, item_id: str) -> Optional[Item]:
        """Returns the Item object with the given id or None if not found

        Parameters
        ----------
        item_id : str
            the id of the item

        Returns
        -------
        Optional[Item]
            the item object with the given id or None if not found
        """
        return self.items.get(item_id)

    def find_banner_by_id(self, banner_id: str) -> Optional[Banner]:
        """Returns the Banner object with the given id or None if not found

        Parameters
        ----------
        banner_id : str
            the id of the banner

        Returns
        -------
        Optional[Banner]
            the banner object with the given id or None if not found
        """
        return self.banners.get(banner_id)

    def find_player_by_id(self, player_id: str) -> Optional[Player]:
        """Returns the Player object with the given id or None if not found

        Parameters
        ----------
        player_id : str
            the id of the player

        Returns
        -------
        Optional[player]
            the player object with the given id or None if not found
        """
        return self.players.get(player_id)

    def pull(self, player_id: str, banner_id: str) -> Optional[Item]:
        """Pulls and returns an item from the specified banner for the specified player

        Parameters
        ----------
        player_id : str
            the id of the selected player
            Preconditon: must be a valid id
        banner_id : str
            the id of the selected banner
            Preconditon: must be a valid id

        Returns
        -------
        Optional[Item]
            the item if the pull is successful or None if the player does not have enough money

        Raises
        ------
        PullError if player or banner are not valid
        """
        player = self.find_player_by_id(player_id)
        if player == None:
            raise PullError("Player not found")
        banner = self.find_banner_by_id(banner_id)
        if banner == None:
            raise PullError("Banner not found")
        if player.change_money(-1 * banner.price):
            item = banner.pull()
            player.add_item(item)
            return item
        return None

    def add_new_item(self, name: str, id: str, rarity: float) -> Optional[Item]:
        """Adds a new item to the gacha game

        Parameters
        ----------
        name : str
            the name of the new item
        id : str
            the id of the new item
            Precondition: must be unique
        rarity : float
            the rarity of the item

        Returns
        -------
        Optional[Item]
            the Item object representing the new item or None if an item
            with the specified id already exists
        """
        item = self.find_item_by_id(id)
        if item != None:
            return None
        new_item = Item(name, id, rarity)
        self.items[id] = new_item
        return new_item

    def add_new_banner(
        self,
        name: str,
        id: str,
        item_list_str: List[str],
        price: float,
        key: Callable[[float], float] = default_key,
    ) -> Optional[Banner]:
        """Adds a new banner to the gacha game

        Parameters
        ----------
        name : str
            the name of the new banner
        id : str
            the id of the new banner
            Precondition: must be unique
        item_list_str : List[str]
            the list of the ids of the items in the banner
        price : float
            the price of pulling from the banner
        key : function : int -> float
            function that takes in rarity and returns the drop rate of the item

        Returns
        -------
        Optional[Banner]
            the Banner object representing the new banner or None if a banner
            with the specified id already exists
        """
        banner = self.find_banner_by_name(name)
        if banner != None:
            return None
        item_list = [self.find_item_by_id(i) for i in item_list_str]
        new_banner = Banner(name, id, item_list, price, key)
        self.banners[id] = new_banner
        return new_banner

    def add_new_player(
        self, name: str, id: str, start_money: float, items_str: List[str] = []
    ) -> Optional[Player]:
        """Adds a new player to the gacha game

        Parameters
        ----------
        name : str
            the name of the new player
        id : str
            the id of the new player
        start_money : float
            the amount of money the new player will start with
        items_str : List[str]
            the list of the ids of the items the player has

        Returns
        -------
        Optional[Player]
            the Player object representing the new player or None if a player
            with the specified id already exists
        """
        player = self.find_player_by_id(id)
        if player != None:
            return None
        items_list = [self.find_item_by_id(i) for i in items_str]
        new_player = Player(name, id, items_list, start_money)
        self.players[id] = new_player
        return new_player

    def remove_item(self, item_id: str) -> Optional[Item]:
        """Removes the specified item from the gacha game
        WARNING: Will also remove from banners and players if found,
        costly operation

        Parameters
        ----------
        item_id : str
            the name of the item to remove

        Returns
        -------
        Optional[Item]
            the removed item or None if item does not exist
        """
        item = self.items.pop(item_id, None)
        if item == None:
            return item
        for banner in self.banners:
            for item in banner.items:
                if item.id == item_id:
                    banner.items.remove(item)
        for player in self.players:
            for item in player.items:
                if item.id == item_id:
                    player.items.remove(item)
        return item

    def remove_banner(self, banner_id: str) -> Optional[Banner]:
        """Removes the specified banner from the gacha game

        Parameters
        ----------
        banner_id : str
            the id of the banner to remove

        Returns
        -------
        Optional[Banner]
            the removed banner or None if banner does not exist
        """
        return self.banners.pop(banner_id, None)

    def remove_player(self, player_id: str) -> Optional[Player]:
        """Removes the specified player from the gacha game

        Parameters
        ----------
        player_id : str
            the id of the player to remove

        Returns
        -------
        Optional[Player]
            the removed player or None if player does not exist
        """
        return self.players.pop(player_id, None)

    def create_random_banner(
        self,
        name: str,
        id: str,
        num_items: int,
        price: float = -1,
        key: Callable[[int], float] = default_key,
    ) -> Optional[Banner]:
        """Creates a random banner with the given name and number of items
            The price is automatically determined by the average of the rarities of the items
            selected if a price is not specified

        Parameters
        ----------
        name : str
            the name of the random banner
        id : str
            the id of the random banner
            Precondition: must be unique
        num_items : int
            the number of items in the banner
        price : float
            the price of the banner
        key : function : int -> float
            function that takes in rarity and returns the drop rate of the item

        Returns
        -------
        Optional[Banner]
            the banner created or None if a banner with the name specified already exists
        """
        item_list = random.choices(list(self.items.values()), k=num_items)
        item_list_str = [item.id for item in item_list]
        if price < 0:
            price = 0
            for item in item_list:
                price += item.rarity
            price /= len(item_list)
        return self.add_new_banner(name, id, item_list_str, price, key)

    def remove_all_banners(self) -> None:
        """Removes all of the banners in the game

        Returns
        -------
        None
        """
        self.banners = {}

    def top_items(self, num_items: int) -> List[Item]:
        """Returns the top specified number of items in the game sorted by rarity

        Parameters
        ----------
        num_items : int
            the number of items to return

        Returns
        -------
        List[Item]
            the list of top items
        """
        sort_list = sorted(list(self.items.values()), key=_sort_item_key, reverse=True)
        return sort_list[: num_items - 1]

    def top_players(self, num_players: int) -> List[Player]:
        """Returns the top specified number of players in the game sorted by net worth

        Parameters
        ----------
        num_players : int
            the number of players to return

        Returns
        -------
        List[Player]
            the list of top players
        """
        sort_list = sorted(
            list(self.players.values()), key=_sort_player_key, reverse=True
        )
        return sort_list[: num_players - 1]
