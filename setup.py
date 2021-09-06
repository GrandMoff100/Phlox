from setuptools import setup
from phlox import (
    __version__,
    __author__,
    __author_email__,
    __description__,
    __name__
)

setup(
    name=__name__,
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    packages=[
        "phlox",
        "phlox.elements",
        "phlox.elements.text",
        "phlox.elements.resources",
        "phlox.ply",
        "phlox.scripting",
        "phlox.styling",
        "phlox.browser"
    ],
    install_requires=[
        "colorama",
        "termcolor",
        "colored",
        "asyncclick",
        "anyio",
        "aiodns",
        "cchardet",
        "aiohttp",
        "aiofiles",
        "aioconsole"
    ],
    description=__description__,
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': 'phlox=phlox.browser:cli'
    }
)
