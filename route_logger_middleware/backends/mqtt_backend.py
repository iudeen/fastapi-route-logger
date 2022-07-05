import logging
from typing import Optional

from . import QueueBackend

try:
    import mqttools
except ImportError:
    logging.warning("MQTT Library not found. Install using pip install asyncio-mqtt")
    raise


class MQTTBackend(QueueBackend):
    def __init__(self, topic: str,
                 hostname: str,
                 port: int = 1883,
                 # *,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 ):
        self.topic = topic
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    async def send_message(self, message: str):
        async with mqttools.Client(
                host=self.hostname,
                port=self.port,
                username=self.username,
                password=self.password,
        ) as client:
            client.publish(mqttools.Message(
                self.topic,
                message=message.encode()
            ))
