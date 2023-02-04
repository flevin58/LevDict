import yaml
from yaml.loader import SafeLoader
from .levdict_base import LevDict
from pathlib import Path


class LevDictYaml(LevDict):
    def __init__(self, the_dict: dict = {}, /, **kwargs) -> None:
        super().__init__(the_dict, **kwargs)

    def load(self, file: str | Path, force: bool = False) -> None:
        if isinstance(file, str):
            yaml_file = Path(file)
        else:
            yaml_file = file

        if not yaml_file.exists():
            raise FileNotFoundError("Cannot locate the yaml file")

        if len(self) > 0 and not force:
            raise ValueError("Attempt to overwrite data without 'force' flag")

        with yaml_file.open("w") as yh:
            my_dict = yaml.load(yh, Loader=SafeLoader)

        self.from_dict(my_dict)

    def dump(self, file: str | Path, force: bool = False) -> None:
        if isinstance(file, str):
            yaml_file = Path(file)
        else:
            yaml_file = file

        if yaml_file.exists() and not force:
            raise ValueError("Attempt to overwrite file without 'force' flag")

        with yaml_file.open("w") as yh:
            yaml.dump(self, yh)
