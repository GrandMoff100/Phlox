import os
import sys
import atexit
import requests
import datetime

from pathlib import Path
from urllib.parse import urlparse

from rich.console import Console


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
                with open(path, 'r') as f:
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
            print('[FETCHER]', err, 'while reading resource from', str(path))

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
    webpage: Console
    error_log: Console

    app_data_path = Path(os.path.expanduser('~'), '.phlox')
    error_log_path = Path(app_data_path, 'error_logs')

    def __init__(self, index_path, env):
        self.env = env
        self.init_app_data()
        self.fetcher = ResourceFetcher(index_path)
        self.webpage = Console(
            force_terminal=True,
            color_system='auto'
        )
        self.webpage.browser = self
        # sys.stderr = Browser.new_error_log_session()

    def new_error_log_session():
        n = datetime.datetime.now()
        f = open(
            Path(
                Browser.error_log_path,
                'Phlox_error_log_{}-{}-{}.{}.{}.{}.log'.format(
                    n.hour,
                    n.minute,
                    n.second,
                    n.month,
                    n.day,
                    n.year
                )
            ),
            'w'
        )
        atexit.register(f.close)
        return f

    def init_app_data(self):
        if not os.path.exists(self.app_data_path):
            os.mkdir(self.app_data_path)
        if not os.path.exists(self.error_log_path):
            os.mkdir(self.error_log_path)
