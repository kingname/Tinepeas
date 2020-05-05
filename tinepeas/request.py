from dataclasses import dataclass
from typing import Callable


@dataclass
class Request:
    url: str
    headers: dict = None
    callback: Callable = None
    method: str = 'get'
    meta: dict = None
    dont_filter: bool = False
    encoding: str = 'utf-8'

    def __repr__(self):
        return f'url: {self.url}, callback: {self.callback}'

