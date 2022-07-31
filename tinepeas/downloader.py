import asyncio
import aiohttp
from typing import Optional
from concurrent.futures import TimeoutError
from asyncio.queues import Queue, QueueEmpty
from . import Request, Response


class Downloader:
    def __init__(self):
        self.response_queue: asyncio.Queue = Queue()
        self.downloading_count = 0

    def empty(self):
        return self.response_queue.empty()

    async def download(self, request: Request):
        print('request for: ', request.url)
        self.downloading_count += 1
        async with aiohttp.ClientSession() as client:
            try:
                resp = await client.request(request.method,
                                            url=request.url,
                                            headers=request.headers)
            except TimeoutError:
                print(f'请求：{request.url}发生超时！')
                return
            raw_response = await resp.text(encoding=request.encoding)
        response = Response(body=raw_response, request=request)
        await self.response_queue.put(response)
        self.downloading_count -= 1

    def get(self) -> Optional[Response]:
        try:
            response = self.response_queue.get_nowait()
        except QueueEmpty:
            return None
        return response
