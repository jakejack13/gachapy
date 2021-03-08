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