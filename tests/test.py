import unittest
import gachapy.objects

item = gachapy.objects.Item("test","test",1)
banner = gachapy.objects.Banner("btest",[item],1)

class TestGachaObjects(unittest.TestCase) :

    def test_banner(self) :
        self.assertEqual(banner.pull().name,item.name)

unittest.main() 