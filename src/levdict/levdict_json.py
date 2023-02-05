import json
from .levdict_base import LevDict
from pathlib import Path


class LevDictJson(LevDict):
    def __init__(self, json_file: str | Path = "") -> None:
        super().__init__()
        if json_file:
            self.load(json_file)

    def load(self, json_file: str | Path, force: bool = False) -> None:
        if isinstance(json_file, str):
            json_file = Path(json_file)
        elif not isinstance(json_file, Path):
            raise TypeError("Bad parameter type to constructor")

        if not json_file.exists():
            raise FileNotFoundError("Cannot locate the json file")

        if len(self) > 0 and not force:
            raise ValueError("Attempt to overwrite data without 'force' flag")

        with json_file.open("r") as jh:
            data: dict = json.load(jh)
            if not isinstance(data, dict):
                raise ValueError("*** Not a Dict !!! ***")

        self.from_dict(data)

    def dump(self, file: str | Path, force: bool = False) -> None:
        if isinstance(file, str):
            json_file = Path(file)
        else:
            json_file = file

        if json_file.exists() and not force:
            raise ValueError("Attempt to overwrite file without 'force' flag")

        with json_file.open("w") as jh:
            json.dump(self, jh, indent=4)
