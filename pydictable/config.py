from typing import Optional


class ConfigDict:

    def __init__(self, str_strip_whitespace=None, _default: Optional[bool] = False):
        self.str_strip_whitespace = str_strip_whitespace
        self.default = _default
