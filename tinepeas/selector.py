from __future__ import annotations

from typing import List, Union, Any, Iterable
from lxml.html import fromstring, HtmlElement


class SelectorList:
    def __init__(self, selector_list: Iterable[Selector]):
        self._selector_list = list(selector_list)

    def get(self, default: Any = None) -> Any:
        """
        如果有，就返回第一条数据，否则，返回default
        返回第一条数据
        :param default:
        :return:
        """
        if self._selector_list:
            return str(self._selector_list[0])
        return default

    def getall(self) -> List[Union[str, Selector]]:
        return list(self._selector_list)

    def __iter__(self):
        for selector in self._selector_list:
            yield selector

    def __len__(self):
        return len(self._selector_list)


class Selector:
    def __init__(self, html: str = '', selector: HtmlElement = None):
        self.html = html
        self._result: List[Union[HtmlElement, str]] = None
        self._selector: HtmlElement = selector

    def xpath(self, xpath_str: str) -> SelectorList:
        if self._selector is None:
            self._selector = fromstring(self.html)

        selector_list = self._selector.xpath(xpath_str)
        return SelectorList(Selector(selector=x) for x in selector_list)

        # if self._result:
        #     self._result = [x.xpath(xpath_str) for x in self._result]
        # else:
        #     self._result = self._selector.xpath(xpath_str)
        # return self

    def __repr__(self):
        return str(self._selector)

