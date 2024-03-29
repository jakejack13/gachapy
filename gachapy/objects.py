"""Objects used for low level management and data storage of the gacha game. 
These objects store information about items, banners, and players in an easy to
use format. It is recommended to use a Controller found in gachapy.controller
for easy storage and access of these objects unless you know what you're doing
(i.e. threading, etc.)

These objects operate as the Model of a gachapy game 

Author: Jacob Kerr, 2021
"""
from .keylang import *
import random
from typing import List


class Item:
    """A representation of an item in the gacha game.
    An item is something that players can collect and pull from banners. Each
    item must be unique

    Fields
    ------
    name : string
        the name of the item
    id : string
        the id of the item
        Invariant: must be unique
    rarity : int
        rarity of the item where the higher the number, the higher the rarity
        Invariant: must be >= 1
    """

    name: str
    """The name of the item"""
    id: str
    """The id of the item
        Invariant: must be unique"""
    rarity: int
    """Rarity of the item where the higher the number, the higher the rarity
        Invariant: must be >= 1"""

    def __init__(self, name: str, id: str, rarity: float) -> None:
        """Creates an Item object

        Parameters
        ----------
        name : str
            name of the item
        id : str
            id of the item
            Precondition: must be unique
        rarity : float
            rarity of the item where the higher the numer, the higher the rarity
        """
        self.name = name
        self.id = id
        self.rarity = rarity

    def change_rarity(self, rarity: float) -> bool:
        """Changes the rarity of the Item

        Parameters
        ----------
        rarity : float
            new rarity of the item
            Precondition: rarity must be >= 1

        Returns
        -------
        bool
            True if the rarity successfully updated, false otherwise
        """
        if rarity < 1:
            return False
        self.rarity = rarity
        return True

    def __str__(self) -> str:
        return f'{self.name}\nID: {self.id}\nRarity: {self.rarity}'
        
    def __eq__(self, other) -> bool:
        if not isinstance(other, Item):
            return False
        return self.id == other.id


class Banner:
    """A representation of a banner in the gacha game.
    A Banner is where players can choose to spend money in order to obtain
    a random item from the specific item pool presented in the Banner. Each
    Banner (should) contain different items and have different prices than
    other banners to distinguish their offerings

    Fields
    ------
    name : str
        name of the banner
    id : str
        id of the banner
        Invariant: must be unique
    items : List[Item]
        the list of items in the banner
    price : float
        the price of pulling from the banner
    key : str
        function that takes in rarity and returns the drop rate of the item,
        written in KeyLang
    _weights : List[float]
        list of drop weights for items
        Invariant: weights[i] corresponds to items[i]
    """

    name: str
    """Name of the banner"""
    id: str
    """The id of the banner
        Invariant: must be unique"""
    items: List[Item]
    """The list of the items in the banner"""
    price: float
    """The price of pulling from the banner"""
    key: str
    """Function that takes in rarity and returns the drop rate of the item,
        written in keylang"""
    _weights: List[float]
    """List of drop weights for items
        Invariant: weights[i" corresponds to items[i]"""

    def __init__(
        self,
        name: str,
        id: str,
        items: List[Item],
        price: float,
        key: str,
    ) -> None:
        """Creates a Banner object

        Parameters
        ----------
        name : str
            name of the banner
        id : str
            id of the banner
            Precondition: must be unique
        items : List[Item]
            the list of items in the banner
            Precondition: all items must be unique
        price : float
            the price of pulling from the banner
        key : str
            function that takes in rarity and returns the drop rate of the item,
            written in KeyLang
        """
        self.name = name
        self.id = id
        self.items = items
        self.price = price
        self.key = key
        self._weights = _get_random_weights(items, key)

    def add_item(self, item: Item) -> bool:
        """Adds an item to the banner

        Parameters
        ----------
        item : Item
            item to add to the banner

        Returns
        -------
        None
        """
        self.items.append(item)
        self._weights = _get_random_weights(self.items, self.key)

    def remove_item(self, item: Item) -> bool:
        """Removes the first occurence of an item from the banner

        Parameters
        ----------
        item : Item
            item to remove from the banner

        Returns
        -------
        bool
            True if item is found in banner, False if otherwise
        """
        try:
            self.items.remove(item)
            self._weights = _get_random_weights(self.items, self.key)
            return True
        except:
            return False

    def pull(self) -> Item:
        """Returns a random item out of a banner randomized by weight

        Returns
        -------
        Item
            the random item from the pull
        """
        return random.choices(self.items, weights=self._weights, k=1)[0]

    def __str__(self) -> str:
        return f"""{self.name}\n
        ID: {self.id}\n
        Price: {self.price}\n
        Items: {' '.join([str(item) for item in self.items])}"""

    def __eq__(self, other) -> bool:
        if not isinstance(other, Banner):
            return False
        return self.id == other.id


class Player:
    """A representation of a player in the gacha game.
    A Player is someone who can use money to purchase pulls from banners,
    receive items from banners, and collect items. Each Player is unique
    and may own different items from each other

    Fields
    ------
    name : str
        the name of the player
    id : str
        the id of the player
        Invariant: must be unique
    items : List[Item]
        the list of items that the player owns
    money : float
        the amount of money that the player owns
    """

    name: str
    """The name of the player"""
    id: str
    """The id of the player
        Invariant: must be unique"""
    items: List[Item]
    """The list of iterms that the player owns"""
    money: float
    """The amount of money that the player owns"""

    def __init__(self, name: str, id: str, items: List[Item], money: float) -> None:
        """Creates a Player object

        Parameters
        ----------
        name : str
            the name of the player
        id : str
            the id of the player
        items : List[Item]
            the list of items that the player owns
        money : float
            the amount of money that the player owns
        """
        self.name = name
        self.id = id
        self.items = items
        self.money = money

    def add_item(self, item: Item) -> None:
        """Adds an item to the player's inventory

        Parameters
        ----------
        item : Item
            item to add to player inventory

        Returns
        -------
        None
        """
        self.items.append(item)

    def remove_item(self, item: Item) -> bool:
        """Removes an item from the player's inventory

        Parameters
        ----------
        item : Item
            item to add to player inventory

        Returns
        -------
        bool
            True if item is found in inventory, False if not
        """
        try:
            self.items.remove(item)
            return True
        except:
            return False

    def change_money(self, amount: float) -> bool:
        """Adds or removes money from player

        Parameters
        ----------
        amount : float
            the amount to add or remove (positive if add, negative if remove)
            Precondition: if amount removed, leftover amount must be nonnegative

        Returns
        -------
        bool
            True if the amount was able to be added or removed from account
            (does not create a negative money value), False otherwise
        """
        if amount < 0 and self.money + amount < 0:
            return False
        self.money += amount
        return True

    def get_net_worth(self) -> float:
        """Returns the net worth of the player, calculated by the sum of the
        rarities of all of the items they own

        Returns
        -------
        float
            the net worth of the player
        """
        return sum([i.rarity for i in self.items])

    def __str__(self) -> str:
        return f"""{self.name}\n
        ID: {self.id}\n
        Money: {self.money}\n
        Net worth: {self.get_net_worth()}\n
        Top 10 items: {' '.join([str(elem) for elem in sorted(
            self.items, key=_sort_item_key, reverse=True
            )[:10]])}"""

    def __eq__(self, other) -> bool:
        if not isinstance(other, Player):
            return False
        return self.id == other.id


def _sort_item_key(item: Item) -> float:
    """The function used to sort items in a list of items

    Parameters
    ----------
    item : Item
        the item to extract the key from

    Returns
    -------
    float
        the key of the item
    """
    return item.rarity


def _get_random_weights(items, key: str) -> List[float]:
    """Returns the random weights of the items for the random function

    Parameters
    ----------
    items : List[Item]
        list of items to find weights of
    key : str
        function that takes in rarity and returns the drop rate of the item,
        written in KeyLang

    Returns
    -------
    List[float]
        the list of weights of the items
    """
    ast = parse(key)
    weights = []
    for item in items:
        weights.append(interpret(ast,item.rarity))
    return weights