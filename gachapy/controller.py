"""The controller used for all high level management of the gacha game

Classes
Controller
    A controller for an instance of a gacha game

Exceptions
PullError
    An exception thrown when pulling from a banner
"""

from typing import Optional
from gachapy.objects import *

class PullError(Exception) :
    """An exception thrown when pulling from a banner
    """
    pass

class Controller :
    """A controller for an instance of a gacha game

    Fields
    items : List[Item]
        the list of items that are in the item pool for the gacha
    banners : List[Banner]
        the list of banners that are available for the gacha
    players : List[Player]
        the list of players enrolled in the gacha
    
    Methods
    find_item(item_name) : Optional[Item]
        Returns the Item object with the given name or None if not found
    find_banner(banner_name) : Optional[Banner]
        Returns the Banner object with the given name or None if not found
    find_player(player_name) : Optional[Banner]
        Returns the Player object with the given name or None if not found
    pull(player_name,banner_name) : Optional[Item]
        Pulls and returns an item from the specified banner for the specified player
    """

    def __init__(self,items=[],banners=[],players=[]) -> None:
        """Creates an instance of a gacha controller

        Parameters
        items : List[Item]
            the list of items that are in the item pool for the gacha
        banners : List[Banner]
            the list of banners that are available for the gacha
        players : List[Player]
            the list of players enrolled in the gacha
        """
        self.items = items
        self.banners = banners
        self.players = players
    
    def find_item(self, item_name) -> Optional[Item]:
        """Returns the Item object with the given name or None if not found

        Parameters
        item_name : str
            the name of the item
        
        Returns
        Optional[Item]
            the item object with the given name or None if not found 
        """
        items = [i for i in self.items if i.name == item_name]
        if len(items) < 1 :
            return None
        return items[0]
    
    def find_banner(self, banner_name) -> Optional[Banner]:
        """Returns the Banner object with the given name or None if not found

        Parameters
        banner_name : str
            the name of the banner
        
        Returns
        Optional[Banner]
            the banner object with the given name or None if not found 
        """
        banners = [i for i in self.banners if i.name == banner_name]
        if len(banners) < 1 :
            return None
        return banners[0]

    
    def find_player(self,player_name) -> Optional[Player]:
        """Returns the Player object with the given name or None if not found

        Parameters
        player_name : str
            the name of the player
        
        Returns
        Optional[player]
            the player object with the given name or None if not found 
        """
        players = [i for i in self.players if i.name == player_name]
        if len(players) < 1 :
            return None
        return players[0]
    
    def pull(self,player_name,banner_name) -> Optional[Item] :
        """Pulls and returns an item from the specified banner for the specified player

        Parameters
        player_name : str
            the name of the selected player, must be valid
        banner_name : str
            the name of the selected player, must be valid

        Returns
        Optional[Item]
            the item if the pull is successful or None if the player does not have enough money
        
        Raises
        PullError if player or banner are not valid
        """
        player = self.find_player(player_name)
        if player == None :
            raise PullError("Player not found")
        banner = self.find_banner(banner_name)
        if banner == None :
            raise PullError("Banner not found")
        if player.change_money(-1 * banner.price) :
            item = banner.pull()
            player.add_item(item)
            return item
        return None

    def change_money_player(self,player_name,amount) -> bool :
        """Changes the specified player's money by the amount specified

        Parameters
        player_name : str
            the name of the player
        amount : float
            the amount to change the money by (positive for add, negative for subtract)

        Return
        bool
            True if the amount was able to be added or removed from account (does not create 
            negative money value), False otherwise
        """
        player = self.find_player(player_name)
        if player == None :
            return False
        return player.change_money(amount)

    def add_new_item(self,name,description,rarity) -> Optional[Item] :
        """Adds a new item to the gacha game

        Parameters
        name : str
            the name of the new item
        description : str
            the description of the new item
        rarity : int
            the rarity of the item

        Returns
        Optional[Item]
            the Item object representing the new item or None if the item already exists
        """
        item = self.find_item(name)
        if item != None :
            return None
        new_item = Item(name,description,rarity)
        self.items.append(new_item)
        return new_item
    
    def add_new_banner(self,name,item_list_str,modifier,price) -> Optional[Banner] :
        """Adds a new banner to the gacha game

        Parameters
        name : str
            the name of the new banner
        item_list_str : List[str]
            the list of the names of the items in the banner
        modifier : float 
            the rate modifier of the banner
        price : float
            the price of pulling from the banner
        
        Return
        Optional[Banner]
            the Banner object representing the new banner or None if the banner already exists
        """
        banner = self.find_banner(name)
        if banner != None :
            return None
        item_list = [self.find_item(i) for i in item_list_str]
        new_banner = Banner(name,item_list,modifier,price)
        self.banners.append(new_banner)
        return Banner

    def add_new_player(self,name,start_money,items_str=[]) -> Optional[Player] :
        """Adds a new player to the gacha game

        Parameters
        name : str
            the name of the new player
        start_money : float
            the amount of money the new player will start with
        items_str : List[str]
            the list of the names of the items the player has
        
        Returns
        Optional[Player]
            the Player object representing the new player or None if the player already exists
        """
        player = self.find_player(name)
        if player != None :
            return None
        items_list = [self.find_item(i) for i in items_str]
        new_player = Player(name,items_list,start_money)
        self.players.append(new_player)
        return new_player