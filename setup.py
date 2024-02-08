from setuptools import setup, find_packages

from PyPoeApi import poe_client

setup(
    name='PyPoeApi',
    version=poe_client.__version__,
    url='https://github.com/fangyunqing/poe_client',
    author='fyq',
    author_email='245960548@qq.com',
    description='for poe api',
    packages=find_packages(),
    py_modules=['PyPoeApi'],
    install_requires=[
        "aiofiles>=23.2.1",
        "aiohttp>=3.9.3",
        "aiohttp-socks>=0.8.4",
        "aiosignal>=1.3.1",
        "async-timeout>=4.0.3",
        "attrs>=23.2.0",
        "certifi>=2024.2.2",
        "charset-normalizer>=3.3.2",
        "colorama>=0.4.6",
        "docutils>=0.20.1",
        "frozenlist>=1.4.1",
        "idna>=3.6",
        "importlib-metadata>=7.0.1",
        "jaraco.classes>=3.3.0",
        "keyring>=24.3.0",
        "loguru>=0.7.2",
        "markdown-it-py>=3.0.0",
        "mdurl>=0.1.2",
        "more-itertools>=10.2.0",
        "multidict>=6.0.5",
        "nh3>=0.2.15",
        "pkginfo>=1.9.6",
        "PyExecJS>=1.5.1",
        "Pygments>=2.17.2",
        "python-socks>=2.4.4",
        "pywin32-ctypes>=0.2.2",
        "PyYAML>=6.0.1",
        "readme-renderer>=42.0",
        "requests>=2.31.0",
        "requests-toolbelt>=1.0.0",
        "rfc3986>=2.0.0",
        "rich>=13.7.0",
        "six>=1.16.0",
        "twine>=4.0.2",
        "urllib3>=2.2.0",
        "win32-setctime>=1.1.0",
        "yarl>=1.9.4",
        "zipp>=3.17.0",
        "Brotli>=1.1.0"
    ],
)