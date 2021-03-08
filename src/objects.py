import random

class Item :
    """A representation of an item in a gacha game

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

    def __init__(self, name, description, rarity) :
        """Creates an Item object

        Parameters
        name : string
            name of the item
        description : string
            description of the item
        rarity : int
            rarity of the item where the higher the numer, the higher the rarity
        """

        self.name = name
        self.description = description
        self.rarity = rarity

def get_random_weights(items, modifier) :
    """Get the random weights of the items for the random function

    Parameters
    items : Item list
        list of items to find weights of
    modifier : float
        weight modifier of the items

    Returns
    float list
        the list of weights of the items
    """
    weights = []
    for i in range(len(items)) :
        weights.append(1 / items[i].rarity / modifier)
    return weights


class Banner :
    """A representation of a banner in a gacha game

    Fields
    name : string
        name of the banner
    item_list : Item list
        the list of items in the banner 
    modifier: float
        the rate modifier for the banner
    """

    def __init__(self, name, item_list, modifier) :
        """Creates a Banner object

        Parameters
        name : string
            name of the banner
        item_list : Item list
            the list of items in the banner
        modifier : float
            the rate modifier for the banner
        weights : float list
            the list of drop weights
            Invariant: weights[i] is the drop weight for item_list[i]
        """
        
        self.name = name
        self.item_list = item_list
        self.modifier = modifier
        self.weights = get_random_weights(item_list, modifier)

    def add_item(self, item) :
        """Add an item to the banner

        Parameters
        item : Item
            item to add to the banner
        
        Returns
            None
        """
        self.item_list.append(item)
        self.weights = get_random_weights(self.item_list, self.modifier)

    def change_modifier(self, modifier) :
        """Change the modifier of the banner

        Parameters
        modifier : float
            the new modifier of the banner

        Returns
            None
        """
        self.modifier = modifier
        self.weights = get_random_weights(self.item_list, self.modifier)

    def pull(self) :
        """Get a random item out of a banner randomized by weight

        Returns
        Item
            the random item from the pull
        """
        return random.choices(self.item_list, weights=self.weights, k=1)[0]
        