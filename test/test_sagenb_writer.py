
import os
import unittest
import tempfile
import shutil
from sagenb_export.sagenb_reader import (
    NotebookSageNB,
    TextCell, ComputeCell,
)
from sagenb_export.ipynb_writer import IpynbWriter


DOT_SAGE = os.path.join(os.path.dirname(__file__), 'dot_sage')


class ReadSageNB(unittest.TestCase):
    """
    Test various sample notebooks
    """

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='sagenb_export_')
        
    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def tmp_filename(self, name):
        return os.path.join(self.tmp, name)
        
    def test_sage_4(self):
        notebook = NotebookSageNB.find(DOT_SAGE, '_sage_:4')
        ipynb = IpynbWriter(notebook)
        ipynb.write(self.tmp_filename('sage:4.ipynb'))

    def test_aleksandra_slapik_44(self):
        notebook = NotebookSageNB.find(DOT_SAGE, 'aleksandra.slapik:44')
        ipynb = IpynbWriter(notebook)
        ipynb.write(self.tmp_filename('aleksandra_slapik_44.ipynb'))
        ipynb.write(self.tmp_filename(u'WDI projekt - R\xf3\u017cankowski, Kie\u0142pi\u0144ski, Kozok.ipynb'))
