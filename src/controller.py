from typing import Optional
from objects import *

class Controller :
    """A controller for an instance of a gacha game

    Fields
    items : List[Item]
        the list of items that are in the item pool for the gacha
    banners : List[Banner]
        the list of banners that are available for the gacha
    players : List[Player]
        the list of players enrolled in the gacha
    """

    def __init__(self,items,banners,players) -> None:
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
        players = [i for i in self.player if i.name == player_name]
        if len(players) < 1 :
            return None
        return players[0]