import sys
import requests
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


class Requester:
    cookies = {
        'User-Agent': build_user_agent()
    }

    def request(self, uri):
        resp = requests.get(
            uri,
            cookies=self.cookies
        )
        # TODO: Log request and response code
        return resp.content

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
            print(err, 'reading resource from', str(path))

    def get(self, resource):
        path = Path(resource)
        if path.exists():
            return self.read_file(path)
        elif urlparse(resource).scheme.startswith('http'):
            return self.request(resource)
        else:
            return ''


class Browser:
    requester = Requester()
