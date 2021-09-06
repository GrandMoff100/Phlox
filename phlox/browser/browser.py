import sys
import aiofiles
import aiohttp

from aioconsole import aprint
from pathlib import Path
from urllib.parse import urlparse


def build_user_agent():
    app = "Phlox"
    version = "1.0.0"
    platform = sys.platform.capitalize()
    python = "Python {}.{}.{}".forat(
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro,
    )

    return '{}/{} ({} on {})'.format(
        app,
        version,
        python,
        platform
    )


class ResourceFetcher:
    cookies = {
        'User-Agent': build_user_agent()
    }

    def __init__(self, cwd, env):
        self.env = env
        self.cwd = cwd

    async def request(self, uri):
        async with aiohttp.ClientSession(cookies=self.cookies) as session:
            async with session.get(uri) as response:
                # TODO: Log request and response code
                return await response.read()

    async def read_file(self, path):
        try:
            try:
                async with aiofiles.open(path, 'r') as f:
                    return await f.read()
            except (
                UnicodeDecodeError,
                UnicodeError
            ):
                with aiofiles.open(path, 'rb') as f:
                    return await f.read()
        except (
            OSError,
            IOError,
            PermissionError,
            FileNotFoundError,
            SystemError
        ) as err:
            await aprint(err, 'reading resource from', str(path))

    async def get(self, resource):
        if (path := Path(self.cwd, resource)).exists():
            return await self.read_file(path)
        elif (path := Path(resource)).exists():
            return await self.read_file(path)
        elif urlparse(resource).scheme.startswith('http'):
            return await self.request(resource)
        else:
            return b''


class Browser:
    fetcher = ResourceFetcher()
