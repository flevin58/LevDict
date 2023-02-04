from typing import Any


class LevDict(dict):
    """Class that implements an attribute oriented dictionary"""

    def __init__(self, the_dict: dict = {}, /, **kwargs) -> None:
        super().__init__()
        if kwargs:
            the_dict.update(**kwargs)
        self.from_dict(data=the_dict)

    def from_dict(self, data: dict) -> None:
        if len(data) > 0:
            for key, val in data.items():
                if isinstance(val, dict):
                    self[key] = LevDict(val)
                else:
                    self[key] = val

    def as_dict(self) -> None:
        ret_dict = {}
        if len(self) > 0:
            for key, val in self.items():
                if isinstance(val, LevDict):
                    ret_dict[key] = val.as_dict()
                else:
                    ret_dict[key] = val
        return ret_dict

    def __getattr__(self, __attr: str) -> Any:
        if __attr in self:
            return self[__attr]
        else:
            raise AttributeError(f"No such attribute: {__attr}")

    def __setattr__(self, __attr: str, __value: Any) -> None:
        if isinstance(__value, dict):
            __value = LevDict(__value)
        self[__attr] = __value

    def __delattr__(self, __attr: str) -> None:
        if __attr in self:
            del self[__attr]
        else:
            raise AttributeError(f"No such attribute: {__attr}")
