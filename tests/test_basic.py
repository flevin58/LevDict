import unittest
from src.levdict import LevDict

DICT_1 = {
    "frutta": {
        "pere": 10,
        "mele": 20,
        "banane": 30,
    },
    "verdura": {
        "carote": 10,
        "melanzane": 15,
    },
}


class TestBasic(unittest.TestCase):
    def setUp(self) -> None:
        self.dict1 = LevDict(DICT_1)

    def tearDown(self) -> None:
        super().tearDown()

    def test_init(self):
        self.assertEqual(self.dict1.as_dict(), DICT_1)

        dict2 = LevDict(a=1, b=2)
        self.assertEqual(dict2.a, 1)

    def test_normal_dict(self):
        result = self.dict1["verdura"]
        expected = {
            "carote": 10,
            "melanzane": 15,
        }
        self.assertEqual(result, expected)

        result = self.dict1["frutta"]["mele"]
        expected = 20
        self.assertEqual(result, expected)

    def test_dotted_dict(self):
        result = self.dict1.verdura
        expected = {
            "carote": 10,
            "melanzane": 15,
        }
        self.assertEqual(result, expected)

        result = self.dict1.frutta.mele
        expected = 20
        self.assertEqual(result, expected)

    def test_mixed_dict(self):
        result = self.dict1.frutta["mele"]
        expected = 20
        self.assertEqual(result, expected)

        result = self.dict1["frutta"].mele
        expected = 20
        self.assertEqual(result, expected)

    def test_assignment(self):
        new_dict: LevDict = LevDict(self.dict1)
        new_dict.frutta.pere = 1
        new_dict.frutta["mele"] = 0

        result = new_dict.frutta
        expected = {
            "pere": 1,
            "mele": 0,
            "banane": 30,
        }
        self.assertEqual(result, expected)

    def test_simple_update(self):
        self.dict1.frutta.update(pere=88)
        result = self.dict1.frutta
        expected = {
            "pere": 88,
            "mele": 0,
            "banane": 30,
        }
