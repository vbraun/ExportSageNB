import os

from tornado.web import authenticated
from notebook.base.handlers import IPythonHandler
 
from sagenb_export.defaults import DOT_SAGE
from sagenb_export.logger import log
from sagenb_export.sagenb_reader import NotebookSageNB
from sagenb_export.nbextension.jinja2_env import jinja2_env



class ListSageNBHandler(IPythonHandler):
    """
    Return a web page that lists the current SageNB worksheets
    """
    
    def notebook_iter(self):
        dot_sage = os.path.expanduser(DOT_SAGE)
        notebooks = dict(
            (notebook.sort_key, notebook)
            for notebook in NotebookSageNB.all_iter(dot_sage)
        )
        for key in sorted(notebooks.keys()):
            # Skip notebooks with owner _sage_ which come from live
            # documentation and are not real notebooks
            if key[0] == "_sage_":
                continue
            yield notebooks[key]
    
    @authenticated
    def get(self):
        template = jinja2_env.get_template('list_handler.html')
        html = template.render(dict(
            notebooks=tuple(self.notebook_iter()),
        ))
        self.finish(html)
