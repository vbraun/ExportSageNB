import os
import string
from itertools import count

from tornado.web import authenticated
from notebook.base.handlers import IPythonHandler
 
from sagenb_export.defaults import DOT_SAGE
from sagenb_export.logger import log
from sagenb_export.sagenb_reader import NotebookSageNB
from sagenb_export.ipynb_writer import IpynbWriter



def filename_escape(name):
    def escape(ch):
        if ch in string.ascii_letters + string.digits:
            return ch
        else:
            return '_'
    return ''.join(map(escape, name))




class ExportSageNBHandler(IPythonHandler):
    """
    Return a web page that lists the current SageNB worksheets
    """

    @property
    def dot_sage(self):
        return os.path.expanduser(DOT_SAGE)
        
    @authenticated
    def post(self):
        print('POST', self.request, self.request.body)
        ipynb_filename = self.safe_filename()
        IpynbWriter(self.notebook()).write(ipynb_filename)
        relative_url = '/notebooks/' + ipynb_filename
        self.finish(relative_url)

    @property
    def unique_id(self):
        return self.request.body
        
    def notebook(self):
        try:
            nb = self._notebook
        except AttributeError:
            nb = self._notebook = NotebookSageNB.find(self.dot_sage, self.unique_id)
        return nb
    
    def safe_filename(self):
        basename = filename_escape(self.notebook().name)
        filename = '{0}.ipynb'.format(basename)
        if not os.path.exists(filename):
            return filename
        for i in count(2):
            filename = '{0} ({1}).ipynb'.format(basename, i)
            if not os.path.exists(filename):
                return filename
    
