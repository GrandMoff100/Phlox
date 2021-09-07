import sys
import asyncclick as click


class StdoutClient:
    def __init__(self):
        pass

    async def clear(self):
        await click.clear()

    async def new_frame(self, frame: str):
        await self.clear()
        await click.echo(
            frame,
            nl=False
        )


class StdinClient:
    async def read_key(self):
        return await click.getchar()
