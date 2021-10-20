import re
import zipfile
from bs4 import BeautifulSoup

reg = re.compile(r'.*(taxonomy.*lab.xml$)')


class ZipUtil:
    def __init__(self, path: str):
        self.path = path

    def namelist(self):
        with zipfile.ZipFile(self.path) as archive:
            for p in archive.namelist():
                if re.match(reg, p):
                    yield p

    def each_soup(self):
        with zipfile.ZipFile(self.path) as archive:
            for child_name in archive.namelist():
                m = re.match(reg, child_name)
                if m:
                    place = m.group(1)
                    with archive.open(child_name) as f:
                        yield BeautifulSoup(f, 'lxml'), place
