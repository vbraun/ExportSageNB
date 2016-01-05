
from tornado.web import StaticFileHandler

from notebook.utils import url_path_join

from sagenb_export.nbextension.list_handler import ListSageNBHandler
from sagenb_export.nbextension.export_handler import ExportSageNBHandler
from sagenb_export.nbextension.asset_handler import AssetHandler




def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    def url(path):
        return url_path_join(web_app.settings['base_url'], path)
    web_app.add_handlers(
        host_pattern, [
            (url(r'/sagenb'), ListSageNBHandler),
            (url(r'/sagenb/export'), ExportSageNBHandler),
            (url(r'/sagenb/www/(.*)'), AssetHandler),
        ]
    )


