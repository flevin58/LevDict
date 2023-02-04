import toml
from .levdict_base import LevDict
from pathlib import Path


class LevDictToml(LevDict):
    def __init__(self, the_dict: dict = {}, /, **kwargs) -> None:
        super().__init__(the_dict, **kwargs)

    def load(self, file: str | Path, force: bool = False) -> None:
        if isinstance(file, str):
            toml_file = Path(file)
        else:
            toml_file = file

        if not toml_file.exists():
            raise FileNotFoundError("Cannot locate the toml file")

        if len(self) > 0 and not force:
            raise ValueError("Attempt to overwrite data without 'force' flag")

        my_dict = toml.load(toml_file)
        self.from_dict(my_dict)

    def dump(self, file: str | Path, force: bool = False) -> None:
        if isinstance(file, str):
            toml_file = Path(file)
        else:
            toml_file = file

        if toml_file.exists() and not force:
            raise ValueError("Attempt to overwrite file without 'force' flag")

        with toml_file.open("w") as tomh:
            toml.dump(self, tomh)
