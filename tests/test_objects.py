"""The test suite for objects.py

Author: Jacob Kerr, 2021
"""
import sys

sys.path.insert(1, ".")

import unittest
from gachapy import *


def test_item_change_rarity(test: unittest.TestCase, item: Item, rarity: float):
    """Asserts that the changed rarity of the item is equal to the inputted
    rarity or if the output is False if the rarity is not valid

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    item : Item
        the item to change the rarity of
    rarity : float
        the rarity to change to
    """
    old_rarity = item.rarity
    result = item.change_rarity(rarity)
    new_rarity = item.rarity
    item.rarity = old_rarity
    if rarity <= 0:
        test.assertFalse(result)
    else:
        test.assertTrue(result)
        test.assertEqual(new_rarity, rarity)


def test_banner_pull(test: unittest.TestCase, banner: Banner, item_id: str):
    """Asserts that the id of the pulled item is equal to the expected item id

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    banner : Banner
        the banner to pull from
    item_id : str
        the id of the expected item
    """
    test.assertEqual(banner.pull().id, item_id)


def test_banner_add_item(test: unittest.TestCase, banner: Banner, item: Item):
    """Asserts that the item specified has been added to the banner
    specified

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    banner : Banner
        the banner to add the item to
    item : Item
        the item to add to the banner
    """
    num_items = len(banner.item_list)
    banner.add_item(item)
    test.assertEqual(len(banner.item_list), num_items + 1)
    test.assertEqual(len(banner.weights), len(banner.item_list))
    test.assertTrue(item in banner.item_list)


def test_banner_remove_item(test: unittest.TestCase, banner: Banner, item: Item):
    """Asserts that the item specified has been removed from the banner
    specified

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    banner : Banner
        the banner to remove the item from
    item : Item
        the item to remove from the banner
    """
    num_items = len(banner.item_list)
    banner.remove_item(item)
    test.assertEqual(len(banner.item_list), num_items - 1)
    test.assertEqual(len(banner.weights), len(banner.item_list))


def test_player_add_item(test: unittest.TestCase, player: Player, item: Item):
    """Assets that the item specified has been added to the player specified

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    player : Player
        the banner to add the item to
    item : Item
        the item to add to the player
    """
    num_items = len(player.items)
    player.add_item(item)
    test.assertEqual(len(player.items), num_items + 1)
    test.assertTrue(item in player.items)


def test_player_remove_item(test: unittest.TestCase, player: Player, item: Item):
    """Assets that the item specified has been removed from the player specified

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    player : Player
        the banner to remove the item from
    item : Item
        the item to remove from the player
    """
    num_items = len(player.items)
    removed = player.remove_item(item)
    test.assertEqual(len(player.items), num_items - 1)
    test.assertTrue(removed)


def test_player_change_money(
    test: unittest.TestCase, player: Player, amount: float, expected: float
):
    """Asserts that the money held in the player's account after a change of
    money is the expected value

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    player : Player
        the player that will have their money changed
    amount : float
        amount to change money by
    expected : float
        the expected amount of money after the change
    """
    player.change_money(amount)
    test.assertEqual(player.money, expected)


def test_player_net_worth(test: unittest.TestCase, player: Player, expected: float):
    """Asserts that the net worth of the specified player is the expected value

    Parameters
    ----------
    test : unittest.TestCase
        the test case to run the test on
    player : Player
        the player to check the net worth of
    expected : float
        the expected net worth value
    """
    test.assertEqual(player.get_net_worth(), expected)


class TestGachaObjects(unittest.TestCase):
    """Test suite for objects.py"""

    def test_item_change_rarity_true(self):
        item = Item("test", "test", 1)
        test_item_change_rarity(self, item, 2)

    def test_item_change_rarity_false(self):
        item = Item("test", "test", 1)
        test_item_change_rarity(self, item, -1)

    def test_banner_add_test_item(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=1,
            key=default_key,
        )
        test_banner_add_item(self, banner, item)

    def test_banner_remove_test_item(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=1,
            key=default_key,
        )
        test_banner_remove_item(self, banner, item)

    def test_banner_pull_test_item(self):
        item = Item("test", "test", 1)
        banner = Banner(
            name="btest",
            id="btest",
            item_list=[item],
            price=1,
            key=default_key,
        )
        test_banner_pull(self, banner, "test")

    def test_player_add_test_item(self):
        item = Item("test", "test", 1)
        player = Player("test", "test", [item], 100)
        test_player_add_item(self, player, item)

    def test_player_remove_test_item(self):
        item = Item("test", "test", 1)
        player = Player("test", "test", [item], 100)
        test_player_add_item(self, player, item)

    def test_player_change_money_true(self):
        player = Player("test", "test", [], 0)
        test_player_change_money(self, player, 50, 50)
        test_player_change_money(self, player, -50, 0)

    def test_player_change_money_false(self):
        player = Player("test", "test", [], 25)
        test_player_change_money(self, player, -30, 25)

    def test_player_net_worth_one_item(self):
        item = Item("test", "test", 1)
        player = Player("test", "test", [item], 100)
        test_player_net_worth(self, player, 1)

    def test_player_net_worth_two_items(self):
        item = Item("test", "test", 1)
        player = Player("test", "test", [item, item], 100)
        test_player_net_worth(self, player, 2)

    def test_player_net_worth_no_items(self):
        player = Player("test", "test", [], 100)
        test_player_net_worth(self, player, 0)


if __name__ == "__main__":
    unittest.main()
