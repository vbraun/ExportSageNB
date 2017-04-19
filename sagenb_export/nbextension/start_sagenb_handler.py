import os
import sys
from subprocess import Popen

from tornado.web import authenticated
from notebook.base.handlers import IPythonHandler

from sagenb_export.nbextension.jinja2_env import jinja2_env


class StartSageNBHandler(IPythonHandler):
    """
    Start the old Sage Notebook server and send its URL.
    """

    @authenticated
    def get(self):
        self.set_header("Content-Type", "text/plain")
        try:
            url = self.sagenb_url()
        except Exception as E:
            self.set_status(500)
            self.finish(str(E))
        else:
            self.finish(url)

    def sagenb_url(self):
        # Run SageNB in a separate process. We create a pipe through
        # which SageNB will communicate the URL.
        rfd, wfd = os.pipe()

        # SageNB will run the command below "$SAGE_BROWSER url"
        # The definition of SAGE_BROWSER below ensures that the url
        # (passed as $0) is written to the write end of the pipe and
        # that both ends of the pipe are then closed.
        env = dict(os.environ)
        env["SAGE_BROWSER"] = "bash -c 'echo >&{1} $0; exec {0}<&- {1}>&-'".format(rfd, wfd)

        # Actually start the Sage notebook
        cmd = "from sagenb.notebook.notebook_object import notebook; notebook()"
        p = Popen([sys.executable, "-c", cmd], stdin=open(os.devnull), env=env)

        # Read URL through the pipe
        os.close(wfd)
        url = os.read(rfd, 1024).strip()
        os.close(rfd)
        if url:
            return url
        else:
            raise RuntimeError("The Sage Notebook failed to start :-(")
