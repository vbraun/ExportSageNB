
import os
from tornado.web import StaticFileHandler

from notebook.base.handlers import FileFindHandler


class AssetHandler(FileFindHandler):

    def initialize(self, **kwds):
        kwds['path'] = [
            os.path.join(os.path.dirname(__file__), 'www'),
        ]
        super(AssetHandler, self).initialize(**kwds)
        
