import unittest
import task2


class Task2TestCase(unittest.TestCase):
    def test_trim(self):
        self.assertEquals(task2.trim("xxxxfexxxxaixxx"), "xxxx")
        self.assertEquals(task2.trim("feaineain"), "aine")
        print("trim OK")

    def test_damage(self):
        self.assertEqual(task2.damage("fexxxx"), 0)
        self.assertEquals(task2.damage("aaa"), 0)
        self.assertEquals(task2.damage('feeai'), 2)
        self.assertEquals(task2.damage('feaineain'), 7)
        self.assertEquals(task2.damage('jee'), 0)
        self.assertEquals(task2.damage('fdafafeajain)'), 1)
        self.assertEquals(task2.damage('fexxxxxxxxxxai'), 0)
        self.assertEquals(task2.damage('fedaiai'), 8)
        self.assertEquals(task2.damage('feainjeeai'),9)
        self.assertEquals(task2.damage('feainjeeainai'), 12)
        print("damage OK")

    def test_is_correct(self):
        self.assertEquals(task2.is_correct("xxxxxfejejeeaindaiyaiaixxxxxx"), True)
        self.assertTrue(task2.is_correct("feeai"))
        print("is correct OK")

    def test_find_subspells(self):
        self.assertEquals(task2.find_subspells("fefeai"), ["fe","fe","ai"])


if __name__ == '__main__':
    unittest.main()
