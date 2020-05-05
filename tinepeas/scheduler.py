from typing import Optional
from collections import deque
from . import Request


class Scheduler:
    def __init__(self):
        self.request_queue = deque()

    def schedule(self, request: Request):
        self.request_queue.append(request)

    def get(self) -> Optional[Request]:
        if self.request_queue:
            return self.request_queue.popleft()
        return None
