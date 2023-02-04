import unittest
from pathlib import Path
from src.levdict import LevDictToml, LevDictJson


class TestLevDict(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.tfile = Path("tests") / "examples" / "example1.toml"
        self.jfile = self.tfile.with_suffix(".json")
        self.yfile = self.tfile.with_suffix(".yaml")
        self.jfile.unlink(missing_ok=True)
        self.yfile.unlink(missing_ok=True)

    def tearDown(self) -> None:
        super().tearDown()

    def test_load(self):
        self.tdict = LevDictToml()
        self.tdict.load(self.tfile)

        self.jdict = LevDictJson(self.tdict)

        result = self.jdict.as_dict()
        expected = self.tdict.as_dict()

        self.assertEqual(result, expected)

    def test_save_partial(self):
        self.tdict = LevDictToml()
        self.tdict.load(self.tfile)

        user: LevDictToml = LevDictToml(self.tdict.user)
        user.dump(self.tfile.with_stem("nando"), force=True)
