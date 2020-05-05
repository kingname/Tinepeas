import uuid
from . import Request
from . import Response
from abc import ABC, abstractmethod


class Spider(ABC):
    name = f'Tinepeas:{uuid.uuid4()}'
    start_urls = []

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    @abstractmethod
    def parse(self, response: Response):
        ...

    def __iter__(self):
        yield from self.start_requests()
