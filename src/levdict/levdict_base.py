from typing import Any

# Forward declarations


class LevDict:
    pass


def _transform_list(data: list) -> list:
    pass


def _transform_tuple(data: tuple) -> tuple:
    pass


def _transform_list(data: list) -> list:
    """
    Returns the modified list with:
    - a LevDict in case of a dict element
    - a transformed tuple
    - a recursive call to itself in case of a list
    - the item if none of the above
    """
    result = []

    for item in data:
        if isinstance(item, dict):
            result.append(LevDict(item))
        elif isinstance(item, list):
            result.append(_transform_list(item))
        elif isinstance(item, tuple):
            result.append(_transform_tuple(item))
        else:
            result.append(item)
    return result


def _transform_tuple(data: tuple) -> tuple:
    """
    Returns the modified tuple with:
    - a LevDict in case of a dict element
    - a transformed list
    - a recursive call to itself in case of a tuple
    - the item if none of the above
    """
    result = ()

    for item in data:
        if isinstance(item, dict):
            result = (*result, LevDict(item))
        elif isinstance(item, list):
            result = (*result, _transform_list(item))
        elif isinstance(item, tuple):
            result = (*result, _transform_tuple(item))
        else:
            result = (*result, item)
    return result


def _transform_dict(data: dict) -> dict:
    """
    Returns the modified dict with:
    - a LevDict in case of a dict element
    - a transformed list
    - a transformed tuple
    - the item if none of the above
    """
    result = {}
    for key, val in data.items():
        if isinstance(val, dict):
            result[key] = LevDict(val)
        elif isinstance(val, list):
            result[key] = _transform_list(val)
        elif isinstance(val, tuple):
            result[key] = _transform_tuple(val)
        else:
            result[key] = val
    return result


class LevDict(dict):
    """Class that implements an attribute oriented dictionary"""

    def __init__(self, the_dict: dict = {}, /, **kwargs) -> None:
        """Constructor: accepts a dict or no arguments"""
        super().__init__()
        if kwargs:
            the_dict.update(**kwargs)
        self.from_dict(data=the_dict)

    def from_dict(self, data: dict) -> None:
        if not isinstance(data, dict):
            raise ValueError("Bad parameter, not a dict!")

        if data:
            data = _transform_dict(data)
            self.update(**data)
            # for key, val in data.items():
            #     if isinstance(val, dict):
            #         self[key] = LevDict(val)
            #     elif isinstance(val, list):
            #         self[key] = __transform_list(val)
            #     else:
            #         self[key] = val

    def as_dict(self) -> None:
        ret_dict = {}
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
