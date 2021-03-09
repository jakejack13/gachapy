from objects import *
from controller import *
from loader import *

def controller_factory(items_filename,banners_filename,players_filename) -> Controller :
    controller = Controller()
    load_items_from_file(items_filename,controller)
    load_banners_from_file(banners_filename,controller)
    load_players_from_file(players_filename,controller)
    return controller