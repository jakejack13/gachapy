"""Objects used for low level management and data storage of the gacha game. 
Instances of these classes should be created indirectly through a Controller 
(see controller.py for more info) but can be modified directly through the use 
of class methods. DO NOT directly edit fields or the invariants could be 
disrupted (although viewing fields directly is permitted). 

These objects operate as the Model of a gachapy game 

Author: Jacob Kerr, 2021
"""
import random
from typing import Callable, List


class Item:
    """A representation of an item in the gacha game.
    An item is something that players can collect and pull from banners. Each
    item must be unique

    Fields
    ------
    name : string
        name of the item
    id : string
        description of the item
        Invariant: must be unique
    id : int
        rarity of the item where the higher the numer, the higher the rarity
        Invariant: must be >= 1
    """

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
        """Returns a string representation of this Item object
        self.name (Rarity: self.rarity)

        Returns
        -------
        str
            String representation of this object
        """
        return self.name + "\nID: " + self.id + "\nRarity: " + str(self.rarity)


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
    item_list : List[Item]
        the list of items in the banner
    price : float
        the price of pulling from the banner
    key : function : int -> float
        function that takes in rarity and returns the drop rate of the item
    weights : List[float]
        list of drop weights for items
        Invariant: weights[i] corresponds to item_list[i]
    """

    def __init__(
        self,
        name: str,
        id: str,
        item_list: List[Item],
        price: float,
        key: Callable[[float], float],
    ) -> None:
        """Creates a Banner object

        Parameters
        ----------
        name : str
            name of the banner
        id : str
            id of the banner
            Precondition: must be unique
        item_list : List[Item]
            the list of items in the banner
            Precondition: all items must be unique
        weights : List[float]
            the list of drop weights
            Precondition: weights[i] is the drop weight for item_list[i]
        price : float
            the price of pulling from the banner
        key : function : int -> float
            function that takes in rarity and returns the drop rate of the item
        """
        self.name = name
        self.id = id
        self.item_list = item_list
        self.key = key
        self.weights = _get_random_weights(item_list, key)
        self.price = price

    def add_item(self, item: Item) -> None:
        """Adds an item to the banner

        Parameters
        ----------
        item : Item
            item to add to the banner

        Returns
        -------
            None
        """
        self.item_list.append(item)
        self.weights = _get_random_weights(self.item_list)

    def remove_item(self, item: Item) -> bool:
        """Removes an item from the banner

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
            self.item_list.remove(item)
            self.weights = _get_random_weights(self.item_list)
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
        return random.choices(self.item_list, weights=self.weights, k=1)[0]

    def __str__(self) -> str:
        """Returns a string representation of this Banner object
        self.name
        Price: self.price
        Items:
        .
        .
        .

        Returns
        -------
        str
            String representation of this object
        """
        return (
            self.name
            + "\nPrice: "
            + str(self.price)
            + "\nItems:\n"
            + "\n".join([str(elem) for elem in self.item_list])
        )


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

    def get_net_worth(self) -> int:
        """Returns the net worth of the player, calculated by the sum of the
        rarities of all of the items they own

        Returns
        -------
        int
            the net worth of the player
        """
        return sum([i.rarity for i in self.items])

    def __str__(self) -> str:
        """Returns a string representation of this Player object
        Money: self.money
        Net worth: self.get_net_worth()
        Top 10 items:
        .
        .
        .
        Top items determined by rarity

        Returns
        -------
        str
            string representation of this object
        """
        return (
            self.name
            + "\n\nMoney: "
            + str(self.money)
            + "\n\nNet worth: "
            + str(self.get_net_worth())
            + "\n\nTop 10 items:\n"
            + "\n".join(
                [
                    str(elem)
                    for elem in sorted(self.items, key=_sort_item_key, reverse=True)[
                        :10
                    ]
                ]
            )
        )


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


def _get_random_weights(items, key: Callable[[float], float]) -> List[float]:
    """Returns the random weights of the items for the random function

    Parameters
    ----------
    items : List[Item]
        list of items to find weights of
    key : function : float -> float
        function that takes in rarity and returns the drop rate of the item

    Returns
    -------
    List[float]
        the list of weights of the items
    """
    weights = []
    for item in items:
        weights.append(key(item.rarity))
    return weights