import asyncio
import importlib
import inspect
from . import Spider
from .core import Core


def run(spider_name):
    spider_module = importlib.import_module(f'spiders.{spider_name}')
    spider = [x for x in inspect.getmembers(spider_module,
                                            predicate=lambda x: inspect.isclass(x)) if issubclass(x[1], Spider)]
    core = Core(spider[0][1])
    asyncio.run(core.start())
