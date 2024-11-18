from abc import ABC, abstractmethod

import aio_pika
from aio_pika.abc import AbstractIncomingMessage, AbstractRobustChannel


class Event(ABC):
    def __init__(self, queue_name: str):
        self.queue_name = queue_name
        self.channel: AbstractRobustChannel | None = None

    async def set_channel(self, channel: AbstractRobustChannel):
        self.channel = channel

    async def publish(self, message: str):
        if self.channel is None:
            raise Exception('Channel is not set')
        await self.channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=self.queue_name
        )

    @abstractmethod
    async def handle(self, message: AbstractIncomingMessage):
        pass
