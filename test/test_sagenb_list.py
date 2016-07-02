# 


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
        self.assertEqual(len(nbks), 4)
        sage_4, admin_4, admin_10, aleks = sorted(nbks)
        self.assertEqual(sage_4.unique_id, '_sage_:4')
        self.assertEqual(sage_4.name, u'Welcome to the Sage Tutorial! -- Sage Tutorial v6.4.rc1')
        self.assertEqual(admin_4.unique_id, 'admin:4')
        self.assertEqual(admin_4.name, u'MathJax_problem1')
        self.assertEqual(admin_10.unique_id, 'admin:10')
        self.assertEqual(admin_10.name, u'Oxford Seminar (1,1)-Calabi Yau')
        self.assertEqual(aleks.unique_id, 'aleksandra.slapik:44')
        self.assertEqual(aleks.name, u'WDI projekt - R\xf3\u017cankowski, Kie\u0142pi\u0144ski, Kozok')

