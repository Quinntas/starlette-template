from typing import Any, Callable, Awaitable

import aio_pika
from aio_pika.abc import AbstractRobustConnection, AbstractIncomingMessage, AbstractRobustChannel

from src.core.event import Event


class EventManager:
    def __init__(self, uri: str):
        self.uri = uri
        self.client: AbstractRobustConnection | None = None
        self.channel: AbstractRobustChannel | None = None

    async def connect(self):
        self.client = await aio_pika.connect_robust(self.uri)
        self.channel = await self.client.channel()

    async def create_queue(self, name: str):
        return await self.channel.declare_queue(name, durable=True)  # type: ignore

    async def subscribe(self, event: Event):
        if self.channel is None:
            raise Exception('Channel is not set')
        await event.set_channel(self.channel)
        await self.consume(event.queue_name, event.handle)

    async def consume(self, queue_name: str, on_message_callback: Callable[[AbstractIncomingMessage], Awaitable[Any]]):
        queue = await self.create_queue(queue_name)
        await queue.consume(on_message_callback, no_ack=True)
