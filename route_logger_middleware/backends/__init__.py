from abc import ABC, abstractmethod


class QueueBackend(ABC):

    @abstractmethod
    async def send_message(self, message: str):
        pass
