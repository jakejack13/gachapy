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
    output : Optional[Player]
        the expected player found
    """
    found_player = controller.find_player_by_name(name)
    test.assertEqual(output, found_player)


class TestGachaObjects(unittest.TestCase):
    """Test suite for controller.py"""

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


if __name__ == "__main__":
    unittest.main()
