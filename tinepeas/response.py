import json
from .request import Request
from .selector import Selector
from dataclasses import dataclass


@dataclass
class Response:
    body: str = ''
    status: int = -1
    request: Request = None
    _selector: Selector = None

    def json(self):
        return json.loads(self.body)

    @property
    def selector(self):
        if not self._selector:
            self._selector = Selector(self.body)
        return self._selector

    def xpath(self, xpath_str):
        return self.selector.xpath(xpath_str)

    @property
    def url(self):
        return self.request.url

    @property
    def meta(self):
        return self.request.meta
