
import os
import unittest
from sagenb_export.sagenb_reader import (
    NotebookSageNB,
    TextCell, ComputeCell,
)


DOT_SAGE = os.path.join(os.path.dirname(__file__), 'dot_sage')

class ListSageNB(unittest.TestCase):

    def test_list(self):
        nbks = list(NotebookSageNB.all_iter(DOT_SAGE))
        self.assertEqual(len(nbks), 3)
        sage_4, admin_4, admin_10 = sorted(nbks)
        self.assertEqual(sage_4.unique_id, '_sage_:4')
        self.assertEqual(sage_4.name, u'Welcome to the Sage Tutorial! -- Sage Tutorial v6.4.rc1')
        self.assertEqual(admin_4.unique_id, 'admin:4')
        self.assertEqual(admin_4.name, u'MathJax_problem1')
        self.assertEqual(admin_10.unique_id, 'admin:10')
        self.assertEqual(admin_10.name, u'Oxford Seminar (1,1)-Calabi Yau')

