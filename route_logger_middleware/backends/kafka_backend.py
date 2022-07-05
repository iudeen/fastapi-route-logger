import logging

from . import QueueBackend

try:
    from aiokafka import AIOKafkaProducer
except ImportError as ime:
    logging.warning(f"Required modules are not available: {ime.name}")
    raise


class KafkaBackend(QueueBackend):
    def __init__(self, kafka_uri: str, topic: str):
        self.kafka_producer = AIOKafkaProducer(bootstrap_servers=kafka_uri)
        self.topic = topic

    async def send_message(self, message: str):
        try:
            await self.kafka_producer.start()
            await self.kafka_producer.send(self.topic, message.encode("utf-8"))
        except Exception as e:
            logging.exception(e)
        finally:
            await self.kafka_producer.stop()
