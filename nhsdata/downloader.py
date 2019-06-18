#!/usr/bin/python3

import requests
import datetime
import os
import sys
from six.moves.urllib.parse import urlparse
from urllib.parse import urlparse

class DataDownloader(object):

    def __init__(self, dataset):
        self._dataset = dataset

    def download(self, block=0):
        block = self._dataset.block(block)
        for s in block.sources():
            dest_path = os.path.join(
                self._dataset.cache(),
                self._dataset.label(),
                block.label(),
                s.label())
            parsed = urlparse(s.url())
            filename = os.path.basename(parsed.path)
            os.makedirs(dest_path)
            r = requests.get(s.url(), allow_redirects=True)
            s.set_localfile(os.path.join(dest_path, filename))
            open(s.localfile(), 'wb').write(r.content)
   