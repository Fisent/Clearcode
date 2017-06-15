import unittest
import task2


class MyTestCase(unittest.TestCase):
    def test_trim(self):
        self.assertEquals(task2.trim("xxxxfexxxxaixxx"), "xxxx")
        self.assertEquals(task2.trim("xxfesssaiaifeai"), "sss")
        print("trim OK")
    def test_damage(self):
        self.assertEqual(task2.damage("fexxxx"), -1)
        self.assertEquals(task2.damage("aaa"), -1)
        print("damage OK")


if __name__ == '__main__':
    unittest.main()
