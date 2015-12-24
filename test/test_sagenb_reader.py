
import os
import unittest
from sagenb_export.sagenb_reader import (
    NotebookSageNB,
    TextCell, ComputeCell,
)


DOT_SAGE = os.path.join(os.path.dirname(__file__), 'dot_sage')

class TestNotebookSageNB(unittest.TestCase):

    def test_list(self):
        nbks = list(NotebookSageNB.all_iter(DOT_SAGE))
        self.assertTrue(len(nbks), 1)

    def test_admin_10(self):
        notebook = NotebookSageNB.find(DOT_SAGE, 'admin:10')
        self.assertEqual(notebook.unique_id, 'admin:10')
        self.assertEqual(notebook.name, 'Oxford Seminar (1,1)-Calabi Yau')
        cell = list(notebook.cells)
        self.assertEqual(len(cell), 37)
        # First cell
        self.assertIsInstance(cell[0], TextCell)
        self.assertEqual(cell[0].input, '<h1 style="text-align: center;">The 24-Cell</h1>')
        # Second cell
        self.assertIsInstance(cell[1], ComputeCell)
        self.assertEqual(cell[1].index, 4)
        self.assertEqual(
            cell[1].input,
            'cell24 = polytopes.twenty_four_cell()\ncell24.f_vector()   # it is self-dual')
        self.assertEqual(cell[1].output, '(1, 24, 96, 96, 24, 1)')
