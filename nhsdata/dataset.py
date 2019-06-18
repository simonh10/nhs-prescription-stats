import json

class DatasetObject(object):

    def __init__(self, config):
        self._config = config

    def name(self):
        return self._config.get('name')

    def label(self):
        return self._config.get('label')


class Dataset(DatasetObject):
    
    def __init__(self, config):
        super().__init__(config)
        self._blocks = self._load_blocks()

    def _load_blocks(self):
        blocks = []
        for b in self._config.get('blocks', []):
            blocks.append(DataBlock(b))
        return blocks

    def blocks(self):
        return self._blocks

    def block(self, index):
        return self._blocks[index]
    
    def block_count(self):
        return len(self._blocks)
    
    def cache(self):
        return self._config.get('cache')
    

class DataBlock(DatasetObject):

    def __init__(self, config):
        super().__init__(config)
        self._localfile = None
        self._downloaded = False
        self._loaded = False
        self._sources = self._load_sources()

    def _load_sources(self):
        sources = []
        for s in self._config.get('sources'):
            sources.append(Datasource(s))
        return sources
    
    def sources(self):
        return self._sources
    
    def load(self):
        pass


class Datasource(DatasetObject):

    def __init__(self, config):
        super().__init__(config)
        self._localfile = None

    def url(self):
        return self._config.get('url')
    
    def localfile(self):
        return self._localfile

    def set_localfile(self, localfile):
        self._localfile = localfile
