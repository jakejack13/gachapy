"""The test suite for controller.py

Author: Jacob Kerr, 2021
"""
import sys

sys.path.insert(1, ".")

import unittest
from gachapy import *


def test_find_item_by_name(
    test: unittest.TestCase, controller: Controller, name: str, output: Optional[Item]
):
    """Asserts that item found by name in the controller is the same as the
    the expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to find the item in
    name : str
        the name of the item
    output : Optional[Item]
        the expected item found
    """
    found_item = controller.find_item_by_name(name)
    test.assertEqual(output, found_item)


def test_find_banner_by_name(
    test: unittest.TestCase, controller: Controller, name: str, output: Optional[Banner]
):
    """Asserts that banner found by name in the controller is the same as the
    the expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to find the banner in
    name : str
        the name of the banner
    output : Optional[Banner]
        the expected banner found
    """
    found_banner = controller.find_banner_by_name(name)
    test.assertEqual(output, found_banner)


def test_find_player_by_name(
    test: unittest.TestCase, controller: Controller, name: str, output: Optional[Player]
):
    """Asserts that player found by name in the controller is the same as the
    the expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to find the player in
    name : str
        the name of the player
    output : Optional[Player]
        the expected player found
    """
    found_player = controller.find_player_by_name(name)
    test.assertEqual(output, found_player)


def test_find_item_by_id(
    test: unittest.TestCase, controller: Controller, id: str, output: Optional[Item]
):
    """Asserts that item found by id in the controller is the same as the
    the expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to find the item in
    id : str
        the id of the item
    output : Optional[Item]
        the expected item found
    """
    found_item = controller.find_item_by_id(id)
    test.assertEqual(output, found_item)


def test_find_banner_by_id(
    test: unittest.TestCase, controller: Controller, id: str, output: Optional[Banner]
):
    """Asserts that banner found by id in the controller is the same as the
    the expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to find the banner in
    id : str
        the id of the banner
    output : Optional[Banner]
        the expected banner found
    """
    found_banner = controller.find_banner_by_id(id)
    test.assertEqual(output, found_banner)


def test_find_player_by_id(
    test: unittest.TestCase, controller: Controller, id: str, output: Optional[Player]
):
    """Asserts that player found by id in the controller is the same as the
    the expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to find the player in
    id : str
        the id of the player
    output : Optional[Player]
        the expected player found
    """
    found_player = controller.find_player_by_id(id)
    test.assertEqual(output, found_player)


def test_pull_valid(
    test: unittest.TestCase,
    controller: Controller,
    player_id: str,
    banner_id: str,
    output: bool,
):
    """Asserts that the item pulled is of a NoneType or not as given by the
    expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to pull from
    player_id : str
        the id of the player to pull to
        Precondition: must be a valid player id in the controller
    banner_id : str
        the id of the banner to pull from
        Precondition: must be a valid banner id in the controller
    output : bool
        True if the output should be a NoneType, False if otherwise
    """
    pulled = controller.pull(player_id, banner_id)
    test.assertEqual(pulled == None, output)


def test_pull_invalid(
    test: unittest.TestCase, controller: Controller, player_id: str, banner_id: str
):
    """Asserts that an exception was thrown from pull due to either a player_id
    or banner_id error

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to pull from
    player_id : str
        the id of the player to pull to, may be invalid
    banner_id : str
        the id of the banner to pull from, may be invalid
    """
    try:
        controller.pull(player_id, banner_id)
        test.assertTrue(False)
    except:
        test.assertTrue(True)


def test_add_new_item(
    test: unittest.TestCase,
    controller: Controller,
    name: str,
    id: str,
    rarity: float,
    output: Optional[Item],
):
    """Asserts that the created item in the controller is equal to the expected
    output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to add the item to
    name : str
        the name of the item
    id : str
        the id of the item
    rarity : float
        the rarity of the item
    output : Optional[Item]
        the expected item to be created
    """
    item = controller.add_new_item(name, id, rarity)
    test.assertEqual(item, output)


def test_add_new_banner(
    test: unittest.TestCase,
    controller: Controller,
    name: str,
    id: str,
    item_list_str: List[str],
    price: float,
    output: Optional[Banner],
):
    """Asserts that the created banner in the controller is equal to the
    expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to add the banner to
    name : str
        the name of the banner
    id : str
        the id of the banner
    item_list_str : List[str]
        the list of ids of the items in the banner
    price : float
        the price of the banner
    output : Optional[Banner]
        the expected banner to be created
    """
    item = controller.add_new_banner(name, id, item_list_str, price)
    test.assertEqual(item, output)


def test_add_new_player(
    test: unittest.TestCase,
    controller: Controller,
    name: str,
    id: str,
    start_money: float,
    output: Optional[Item],
):
    """Asserts that the created player in the controller is equal to the
    expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to add the player to
    name : str
        the name of the player
    id : str
        the id of the player
    start_money : float
        the starting money of the player
    output : Optional[Player]
        the expected player to be created
    """
    player = controller.add_new_player(name, id, start_money)
    test.assertEqual(player, output)


def test_remove_item(
    test: unittest.TestCase,
    controller: Controller,
    item_id: str,
    output: Optional[Item],
):
    """Asserts that the removed item from the controller is equal to the
    expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    item_id : str
        the id of the item to remove
    output : Optional[Item]
        the expected output of remove
    """
    item = controller.remove_item(item_id)
    test.assertEqual(item, output)


def test_remove_banner(
    test: unittest.TestCase,
    controller: Controller,
    banner_id: str,
    output: Optional[Banner],
):
    """Asserts that the removed banner from the controller is equal to the
    expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    banner_id : str
        the id of the banner to remove
    output : Optional[Banner]
        the expected output of remove
    """
    banner = controller.remove_banner(banner_id)
    test.assertEqual(banner, output)


def test_remove_player(
    test: unittest.TestCase,
    controller: Controller,
    player_id: str,
    output: Optional[Player],
):
    """Asserts that the removed player from the controller is equal to the
    expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    player_id : str
        the id of the player to remove
    output : Optional[Item]
        the expected output of remove
    """
    player = controller.remove_player(player_id)
    test.assertEqual(player, output)


def test_create_random_banner(
    test: unittest.TestCase,
    controller: Controller,
    name: str,
    id: str,
    num_items: int,
    output: bool,
):
    """Asserts that the newly created random banner is equal to NoneType
    depending on the expected output

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to create the banner in
    name : str
        the name of the banner
    id : str
        the id of the banner
    num_items : int
        the number of items in the banner
    output : bool
        True if the output should be None, False if otherwise
    """
    banner = controller.create_random_banner(name, id, num_items)
    test.assertEqual(banner == None, output)
    if not output:
        test.assertEqual(banner, controller.find_banner_by_id(id))


def test_remove_all_banners(test: unittest.TestCase, controller: Controller):
    """Asserts that the number of banners left in a controller after removing
    all banners is 0

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to remove banners from
    """
    controller.remove_all_banners()
    test.assertEqual(len(controller.banners), 0)


def test_top_items(test: unittest.TestCase, controller: Controller, num_items: int):
    """Asserts that the length of the returned list of top items is equal to
    the given number of items

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller get top items from
    num_items : int
        the number of top items to retrieve
    """
    top_items = controller.top_items(num_items)
    test.assertEqual(len(top_items), num_items)


def test_top_players(test: unittest.TestCase, controller: Controller, num_players: int):
    """Asserts that the length of the returned list of top players is equal to
    the given number of players

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    controller : Controller
        the controller to get top players from
    num_items : int
        the number of top players to retrieve
    """
    top_players = controller.top_players(num_players)
    test.assertEqual(len(top_players), num_players)


class TestGachaController1(unittest.TestCase):
    """First test suite for controller.py"""

    def test_find_item_by_name_empty(self):
        controller = Controller()
        test_find_item_by_name(self, controller, "test", None)

    def test_find_item_by_name_one_item_none(self):
        item = Item("test", "test", 1)
        controller = Controller(items={"test": item})
        test_find_item_by_name(self, controller, "not_test", None)

    def test_find_item_by_name_one_item_found(self):
        item = Item("test", "test", 1)
        controller = Controller(items={"test": item})
        test_find_item_by_name(self, controller, "test", item)

    def test_find_banner_by_name_empty(self):
        controller = Controller()
        test_find_banner_by_name(self, controller, "test", None)

    def test_find_banner_by_name_one_item_none(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=1,
            key=default_key,
        )
        controller = Controller(items={"test": item}, banners={"btest": banner})
        test_find_banner_by_name(self, controller, "not_test", None)

    def test_find_banner_by_name_one_item_found(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=1,
            key=default_key,
        )
        controller = Controller(items={"test": item}, banners={"btest": banner})
        test_find_banner_by_name(self, controller, "btest", banner)

    def test_find_player_by_name_empty(self):
        controller = Controller()
        test_find_player_by_name(self, controller, "test", None)

    def test_find_player_by_name_one_item_none(self):
        item = Item("test", "test", 1)
        player = Player("ptest", "ptest", [item], 100)
        controller = Controller(items={"test": item}, players={"ptest": player})
        test_find_player_by_name(self, controller, "not_test", None)

    def test_find_player_by_name_one_item_found(self):
        item = Item("test", "test", 1)
        player = Player("ptest", "ptest", [item], 100)
        controller = Controller(items={"test": item}, players={"ptest": player})
        test_find_player_by_name(self, controller, "ptest", player)

    def test_find_item_by_id_empty(self):
        controller = Controller()
        test_find_item_by_id(self, controller, "test", None)

    def test_find_item_by_id_one_item_none(self):
        item = Item("test", "test", 1)
        controller = Controller(items={"test": item})
        test_find_item_by_id(self, controller, "not_test", None)

    def test_find_item_by_id_one_item_found(self):
        item = Item("test", "test", 1)
        controller = Controller(items={"test": item})
        test_find_item_by_id(self, controller, "test", item)

    def test_find_banner_by_id_empty(self):
        controller = Controller()
        test_find_banner_by_id(self, controller, "test", None)

    def test_find_banner_by_id_one_item_none(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=1,
            key=default_key,
        )
        controller = Controller(items={"test": item}, banners={"btest": banner})
        test_find_banner_by_id(self, controller, "not_test", None)

    def test_find_banner_by_id_one_item_found(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=1,
            key=default_key,
        )
        controller = Controller(items={"test": item}, banners={"btest": banner})
        test_find_banner_by_id(self, controller, "btest", banner)

    def test_find_player_by_id_empty(self):
        controller = Controller()
        test_find_player_by_id(self, controller, "test", None)

    def test_find_player_by_id_one_item_none(self):
        item = Item("test", "test", 1)
        player = Player("ptest", "ptest", [item], 100)
        controller = Controller(items={"test": item}, players={"ptest": player})
        test_find_player_by_id(self, controller, "not_test", None)

    def test_find_player_by_id_one_item_found(self):
        item = Item("test", "test", 1)
        player = Player("ptest", "ptest", [item], 100)
        controller = Controller(items={"test": item}, players={"ptest": player})
        test_find_player_by_id(self, controller, "ptest", player)

    def test_pull_one_item_success(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=1,
            key=default_key,
        )
        player = Player("ptest", "ptest", [item], 100)
        controller = Controller(
            items={"test": item}, banners={"btest": banner}, players={"ptest": player}
        )
        test_pull_valid(self, controller, "ptest", "btest", False)

    def test_pull_one_item_no_money(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=100,
            key=default_key,
        )
        player = Player("ptest", "ptest", [item], 1)
        controller = Controller(
            items={"test": item}, banners={"btest": banner}, players={"ptest": player}
        )
        test_pull_valid(self, controller, "ptest", "btest", True)

    def test_pull_player_error(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=100,
            key=default_key,
        )
        player = Player("ptest", "ptest", [item], 1)
        controller = Controller(
            items={"test": item}, banners={"btest": banner}, players={"ptest": player}
        )
        test_pull_invalid(self, controller, "ptest1", "btest")

    def test_pull_banner_error(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=100,
            key=default_key,
        )
        player = Player("ptest", "ptest", [item], 1)
        controller = Controller(
            items={"test": item}, banners={"btest": banner}, players={"ptest": player}
        )
        test_pull_invalid(self, controller, "ptest", "btest1")

    def test_pull_both_error(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=100,
            key=default_key,
        )
        player = Player("ptest", "ptest", [item], 1)
        controller = Controller(
            items={"test": item}, banners={"btest": banner}, players={"ptest": player}
        )
        test_pull_invalid(self, controller, "ptest1", "btest1")


class TestGachaController2(unittest.TestCase):
    """Second test suite for controller.py"""

    def test_add_item_empty(self):
        item = Item("test", "test", 1)
        controller = Controller()
        test_add_new_item(self, controller, "test", "test", 1, item)

    def test_add_item_full(self):
        item = Item("test", "test", 1)
        controller = Controller(items={"test": item})
        test_add_new_item(self, controller, "test", "test", 1, None)

    def test_add_banner_empty(self):
        item = Item("test", "test", 1)
        controller = Controller(items={"test": item})
        banner = Banner("btest", "btest", [item], 100, default_key)
        test_add_new_banner(self, controller, "btest", "btest", ["test"], 100, banner)

    def test_add_banner_full(self):
        item = Item("test", "test", 1)
        banner = Banner("btest", "btest", [item], 100, default_key)
        controller = Controller(items={"test": item}, banners={"btest": banner})
        test_add_new_banner(self, controller, "btest", "btest", ["test"], 100, None)

    def test_add_player_empty(self):
        player = Player("ptest", "ptest", [], 100)
        controller = Controller()
        test_add_new_player(self, controller, "ptest", "ptest", 100, player)

    def test_add_player_full(self):
        player = Player("ptest", "ptest", [], 100)
        controller = Controller(players={"ptest": player})
        test_add_new_player(self, controller, "ptest", "ptest", 100, None)

    def test_remove_item_full(self):
        item = Item("test", "test", 1)
        controller = Controller(items={"test": item})
        test_remove_item(self, controller, "test", item)

    def test_remove_banner_full(self):
        item = Item("test", "test", 1)
        banner = Banner("btest", "btest", [item], 100, default_key)
        controller = Controller(items={"test": item}, banners={"btest": banner})
        test_remove_banner(self, controller, "btest", banner)

    def test_remove_player_full(self):
        player = Player("ptest", "ptest", [], 100)
        controller = Controller(players={"ptest": player})
        test_remove_player(self, controller, "ptest", player)

    def test_remove_item_empty(self):
        controller = Controller()
        test_remove_item(self, controller, "notest", None)

    def test_remove_banner_empty(self):
        controller = Controller()
        test_remove_banner(self, controller, "notest", None)

    def test_remove_player_empty(self):
        controller = Controller()
        test_remove_player(self, controller, "notest", None)

    def test_create_random_banner_empty(self):
        item = Item("test", "test", 1)
        controller = Controller(items={"test": item})
        test_create_random_banner(self, controller, "1btest", "1btest", 1, False)

    def test_create_random_banner_full(self):
        item = Item("test", "test", 1)
        banner = Banner("2btest", "2btest", [item], 100, default_key)
        controller = Controller(items={"test": item}, banners={"2btest": banner})
        test_create_random_banner(self, controller, "2btest", "2btest", 1, True)

    def test_remove_all_banners_empty(self):
        controller = Controller()
        test_remove_all_banners(self, controller)

    def test_remove_all_banners_full(self):
        item = Item("test", "test", 1)
        banner = Banner("3btest", "3btest", [item], 100, default_key)
        controller = Controller(items={"test": item}, banners={"3btest": banner})
        test_remove_all_banners(self, controller)

    def test_top_items_one(self):
        item = Item("test", "test", 1)
        controller = Controller(items={"test": item})
        test_top_items(self, controller, 1)

    def test_top_players_one(self):
        item = Item("test", "test", 1)
        player = Player("ptest", "ptest", [item], 100)
        controller = Controller(items={"test": item}, players={"ptest": player})
        test_top_players(self, controller, 1)


if __name__ == "__main__":
    unittest.main()
