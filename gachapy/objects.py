"""Objects used for low level management and data storage of the gacha game

Classes
Item
    A representation of an item in the gacha game
Banner
    A representation of a banner in the gacha game
Player
    A representation of a player in the gacha game

Functions
get_random_weights(items) : List[float]
    Returns the random weights of the items for the random function
sort_item_key(item) : int
    The key used to sort items in a list of items
player_str_net_worth(player) : str
    The string representation of a player and their net worth
"""
import random
from typing import List

class Item :
    """A representation of an item in the gacha game

    Fields
    name : string
        name of the item
    id : string
        description of the item
        Invariant: must be unique
    id : int
        rarity of the item where the higher the numer, the higher the rarity

    Methods
    Item : Item
        creates an item object
    """

    def __init__(self, name, id, rarity) -> None :
        """Creates an Item object

        Parameters
        name : str
            name of the item
        id : str
            id of the item
        rarity : int
            rarity of the item where the higher the numer, the higher the rarity
        """
        self.name = name
        self.id = id
        self.rarity = rarity
    
    def __str__(self) -> str :
        """Returns the string representation of this Item object

        Returns
        str
            String representation of this object
        """
        return self.name + " (Rarity: " + str(self.rarity) + ")"

def get_random_weights(items,key) -> List[float] :
    """Returns the random weights of the items for the random function

    Parameters
    items : List[Item]
        list of items to find weights of
    key : func
        function that determines drop rate from rarity

    Returns
    List[float]
        the list of weights of the items
    """
    weights = []
    for i in range(len(items)) :
        weights.append(key(items[i].rarity))
    return weights


class Banner :
    """A representation of a banner in the gacha game

    Fields
    name : string
        name of the banner
    item_list : List[Item]
        the list of items in the banner 
    price : float
        the price of pulling from the banner
    key : func
        function that determines drop rate from rarity
    weights : List[float]
        list of drop weights for items
        Invariant: weights[i] corresponds to item_list[i]

    Methods
    add_item(item) : None
        Adds an item to the banner
    pull() : Item
        Returns a random item out of a banner randomized by weight
    """

    def __init__(self, name, item_list, price, key) -> None :
        """Creates a Banner object

        Parameters
        name : str
            name of the banner
            Invariant: must be unique
        item_list : List[Item]
            the list of items in the banner
            Invariant: all items must be unique
        weights : List[float]
            the list of drop weights
            Invariant: weights[i] is the drop weight for item_list[i]
        price : float
            the price of pulling from the banner
        key : func
            function that determines drop rate from rarity

        """
        self.name = name
        self.item_list = item_list
        self.key = key
        self.weights = get_random_weights(item_list,key)
        self.price = price

    def add_item(self, item) -> None:
        """Adds an item to the banner

        Parameters
        item : Item
            item to add to the banner
        
        Returns
            None
        """
        self.item_list.append(item)
        self.weights = get_random_weights(self.item_list)

    def pull(self) -> Item:
        """Returns a random item out of a banner randomized by weight

        Returns
        Item
            the random item from the pull
        """
        return random.choices(self.item_list, weights=self.weights, k=1)[0]

    def __str__(self) -> str :
        """Returns the string representation of this Banner object

        Returns
        str
            String representation of this object
        """
        return self.name + "\nPrice: " + str(self.price) + "\nItems:\n" + "\n".join([str(elem) for elem in self.item_list])

class Player :
    """A representation of a player in the gacha game

    Fields
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

    def __init__(self, name, id, items, money) -> None:
        """Creates a Player object

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
    
    def add_item(self,item) -> None:
        """Adds an item to the player's inventory

        Parameters
        item : Item
            item to add to player inventory

        Returns
        None
        """
        self.items.append(item)

    def change_money(self,amount) -> bool:
        """Adds or removes money from player

        Parameters
        amount : float
            the ammount to add or remove (positive if add, negative if remove)

        Return
        bool
            True if the amount was able to be added or removed from account (does not
            create a negative money value), False otherwise
        """
        if (amount < 0 and self.money - amount < 0) :
            return False
        self.money += amount
        return True

    def get_net_worth(self) -> float :
        """Returns the net worth of the player

        Returns
        float
            the net worth of the player
        """
        return sum([i.rarity for i in self.items])
    
    def __str__(self) -> str:
        """Returns the string representation of this Player object

        Returns
        str
            string representation of this object
        """
        return self.name + "\n\nMoney: " + str(self.money) + "\n\nNet worth: " + str(self.get_net_worth()) + "\n\nTop 10 items:\n" + "\n".join([str(elem) for elem in sorted(self.items,key=sort_item_key,reverse=True)[:10]])

def sort_item_key(item) -> int:
    """The key used to sort items in a list of items

    Parameters
    item : Item
        the item to extract the key from
    
    Returns
    int
        the key of the item
    """
    return item.rarity

def player_str_net_worth(player) -> str :
    """The string representation of a player and their net worth

    Parameters
    player : Player
        the player
    
    Returns
    str
        the string representation of a player and their net work
    """
    return player.name + " (Net worth " + str(player.get_net_worth()) + ")"