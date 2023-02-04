import json
from .levdict_base import LevDict
from pathlib import Path


class LevDictJson(LevDict):
    def __init__(self, the_dict: dict = {}, /, **kwargs) -> None:
        super().__init__(the_dict, **kwargs)

    def load(self, file: str | Path, force: bool = False) -> None:
        if isinstance(file, str):
            json_file = Path(file)
        else:
            json_file = file

        if not json_file.exists():
            raise FileNotFoundError("Cannot locate the json file")

        if len(self) > 0 and not force:
            raise ValueError("Attempt to overwrite data without 'force' flag")

        with json_file.open("w") as jh:
            my_dict = json.load(jh)

        self.from_dict(my_dict)

    def dump(self, file: str | Path, force: bool = False) -> None:
        if isinstance(file, str):
            json_file = Path(file)
        else:
            json_file = file

        if json_file.exists() and not force:
            raise ValueError("Attempt to overwrite file without 'force' flag")

        with json_file.open("w") as jh:
            json.dump(self, jh, indent=4)
