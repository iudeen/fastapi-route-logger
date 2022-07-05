import json
import pprint
import asyncio
from . import QueueBackend


class PrintBackend(QueueBackend):

    async def send_message(self, message: str):
        await asyncio.sleep(4)
        pprint.pprint(json.loads(message))
