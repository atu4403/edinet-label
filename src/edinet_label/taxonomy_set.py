import pathlib
import bs4
from typing import Generator
from .zip_util import ZipUtil
from .redis_adapter import redis_client


def _each_values(soup: bs4.BeautifulSoup, place: str) -> Generator:
    for label in soup.find_all('link:label'):
        _, name = label.attrs['id'].split('label_')
        value = label.get_text()
        yield place, name, value


def _all_files_each_values(zip_dir: str) -> Generator:
    for path in pathlib.Path(zip_dir).iterdir():
        for soup, place in ZipUtil(path).each_soup():
            for tup in _each_values(soup, place):
                yield tup


def set_redis(zip_dir: str):
    pipe = redis_client().pipeline()
    for tup in _all_files_each_values(zip_dir):
        pipe.hset(*tup)
    pipe.execute()
