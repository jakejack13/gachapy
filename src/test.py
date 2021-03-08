import unittest
import objects

item = objects.Item("test","test",1)
banner = objects.Banner("btest",[item],1)

class TestGachaObjects(unittest.TestCase) :
    
    def test_banner(self) :
        self.assertEqual(banner.pull().name,item.name)

unittest.main()