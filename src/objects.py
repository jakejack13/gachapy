"""Objects used for the gacha game

Classes
Item
    A representation of an item in the gacha game
Banner
    A representation of a banner in the gacha game
Player
    A representation of a player in the gacha game

Functions
    get_random_weights(items,modifier) : List[float]
        Returns the random weights of the items for the random function
"""
import random
from typing import List

class Item :
    """A representation of an item in the gacha game

    Fields
    name : string
        name of the item
    description : string
        description of the item
    rarity : int
        rarity of the item where the higher the numer, the higher the rarity

    Methods
    Item : Item
        creates an item object
    """

    def __init__(self, name, description, rarity) -> None :
        """Creates an Item object

        Parameters
        name : str
            name of the item
        description : str
            description of the item
        rarity : int
            rarity of the item where the higher the numer, the higher the rarity
        """
        self.name = name
        self.description = description
        self.rarity = rarity
    
    def __str__(self) -> str :
        """Returns the string representation of this Item object

        Returns
        str
            String representation of this object
        """
        return self.name + "\n" + self.description + "\n" + "Rarity: " + str(self.rarity)

def get_random_weights(items, modifier) -> List[float] :
    """Returns the random weights of the items for the random function

    Parameters
    items : List[Item]
        list of items to find weights of
    modifier : float
        weight modifier of the items

    Returns
    List[float]
        the list of weights of the items
    """
    weights = []
    for i in range(len(items)) :
        weights.append(1 / items[i].rarity / modifier)
    return weights


class Banner :
    """A representation of a banner in the gacha game

    Fields
    name : string
        name of the banner
    item_list : List[Item]
        the list of items in the banner 
    modifier: float
        the rate modifier for the banner
    price : float
        the price of pulling from the banner

    Methods
    add_item(item) : None
        Adds an item to the banner
    change_modifier(modifier) : None
        Changes the modifier of the banner
    pull() : Item
        Returns a random item out of a banner randomized by weight
    """

    def __init__(self, name, item_list, modifier, price) -> None :
        """Creates a Banner object

        Parameters
        name : string
            name of the banner
            Invariant: must be unique
        item_list : List[Item]
            the list of items in the banner
            Invariant: all items must be unique
        modifier : float
            the rate modifier for the banner
        weights : List[float]
            the list of drop weights
            Invariant: weights[i] is the drop weight for item_list[i]
        price : float
            the price of pulling from the banner
        """
        self.name = name
        self.item_list = item_list
        self.modifier = modifier
        self.weights = get_random_weights(item_list, modifier)
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
        self.weights = get_random_weights(self.item_list, self.modifier)

    def change_modifier(self, modifier) -> None :
        """Changes the modifier of the banner

        Parameters
        modifier : float
            the new modifier of the banner

        Returns
            None
        """
        self.modifier = modifier
        self.weights = get_random_weights(self.item_list, self.modifier)

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
        return self.name + "\n".join([str(elem) for elem in self.item_list])

class Player :
    """A representation of a player in the gacha game

    Fields
    name : str
        the name of the player
    items : List[Item]
        the list of items that the player owns
    money : float
        the amount of money that the player owns
    """

    def __init__(self, name, items, money) -> None:
        self.name = name
        self.items = items
        self.money = money
    
    def add_item(self,item) -> bool:
        """Adds an item to the player's inventory

        Parameters
        item : Item
            item to add to player inventory

        Returns
        bool
            True if item is not already in player's inventory, False otherwise
        """
        matching = [i for i in self.items if i.name == item.name]
        if len(matching) > 0 :
            return False
        self.items.append(item)
        return True

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
        if (self.money - amount < 0) :
            return False
        self.money += amount
        return True
    
    def __str__(self) -> str:
        """Returns the string representation of this Player object

        Returns
        str
            string representation of this object
        """
        return self.name + "\n".join([str(elem) for elem in self.items]) + "Money: " + str(self.money)