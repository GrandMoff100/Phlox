import os
import sys
import requests

from pathlib import Path
from urllib.parse import urlparse


def build_user_agent():
    app = "Phlox"
    version = "1.0.0"
    platform = sys.platform.capitalize()
    python = "Python {}.{}.{}".format(
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
    @property
    def cookies(self):
        return {
            'User-Agent': build_user_agent()
        }

    def __init__(self, cwd):
        self.cwd = cwd

    def request(self, uri):
        return requests.get(uri, cookies=self.cookies).content

    def read_file(self, path):
        try:
            try:
                async with open(path, 'r') as f:
                    return f.read()
            except (
                UnicodeDecodeError,
                UnicodeError
            ):
                with open(path, 'rb') as f:
                    return f.read()
        except (
            OSError,
            IOError,
            PermissionError,
            FileNotFoundError,
            SystemError
        ) as err:
            print(err, 'reading resource from', str(path))

    def get(self, resource):
        if urlparse(resource).scheme.startswith('http'):
            return self.request(resource)
        elif urlparse(uri := os.path.join(self.cwd, resource)).scheme.startswith('http'):
            return self.request(uri)
        elif (path := Path(self.cwd, resource)).exists():
            return self.read_file(path)
        elif (path := Path(resource)).exists():
            return self.read_file(path)


class Browser:
    def __init__(self, index_path, env):
        self.env = env
        self.fetcher = ResourceFetcher(index_path)
