
import os
import unittest
from sagenb_export.sagenb_reader import (
    NotebookSageNB,
    TextCell, ComputeCell,
)


try:
    string_type = unicode  # py2
except NameError:
    string_type = str  # py3

    
DOT_SAGE = os.path.join(os.path.dirname(__file__), 'dot_sage')


class ReadSageNB(unittest.TestCase):
    """
    Test various sample notebooks
    """

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
        self.assertEqual(cell[1].input, cell[1].ipython_input())
        self.assertEqual(cell[1].output, '(1, 24, 96, 96, 24, 1)')
        self.assertEqual(cell[1].plain_text_output(), '(1, 24, 96, 96, 24, 1)')
        # Third cell (containing HTML)
        self.assertIsInstance(cell[2], ComputeCell)
        self.assertEqual(cell[2].index, 86)
        self.assertEqual(
            cell[2].input, 'cell24.f_vector?')
        self.assertEqual(cell[2].input, cell[2].ipython_input())
        self.assertIn('<html><!--notruncate-->\n\n<div class="docstring">', cell[2].output)
        self.assertEqual(cell[2].plain_text_output(), '')

    def test_sage_4(self):
        notebook = NotebookSageNB.find(DOT_SAGE, '_sage_:4')
        self.assertEqual(notebook.unique_id, '_sage_:4')
        self.assertEqual(notebook.name, 'Welcome to the Sage Tutorial! -- Sage Tutorial v6.4.rc1')
        cell = list(notebook.cells)
        self.assertEqual(len(cell), 2)
        self.assertEqual(type(cell[0].input), string_type)
        self.assertEqual(type(cell[1].input), string_type)
        self.assertEqual(type(cell[1].output), string_type)

    def test_admin_4(self):
        notebook = NotebookSageNB.find(DOT_SAGE, 'admin:4')
        self.assertEqual(notebook.unique_id, 'admin:4')
        self.assertEqual(notebook.name, u'MathJax_problem1')
        cell_list = list(notebook.cells)
        self.assertEqual(len(cell_list), 2)
        # First cell
        cell0 = cell_list[0]
        self.assertIsInstance(cell0, TextCell)
        self.assertEqual(cell0.input, u'<h2>R\xf3wnanie Newtona</h2>\n<h2>$$\\vec F= m\\vec a$$\xa0</h2>\n<p>Rzut pionowy</p>\n<p>$$F= m a$$\xa0</p>\n<p>\xa0</p>\n<h2>\xa0Krok czasowy: $\\Delta t$.</h2>\n<p>\xa0</p>\n<ul>\n<li>$ \xa0v\xa0=\xa0\\displaystyle\\frac{ \\Delta \xa0y}{\\Delta t}$</li>\n</ul>\n<ul>\n<li>$ \xa0a\xa0=\xa0 \\displaystyle \\frac{\\Delta \xa0v}{\\Delta t}$</li>\n</ul>\n<div>\xa0</div>\n<p>$$\\begin{cases} \\quad \\displaystyle \\frac{\\Delta y}{\\Delta t} &=& v \\\\ \\quad \\displaystyle \\frac{\\Delta v}{\\Delta t} &=& \\displaystyle \\frac { F}{m} \\end{cases} $$</p>\n<p>\xa0</p>\n<p>\xa0</p>\n<div>\xa0$\\:y_0\\:$ \xa0i $\\:v_{0}\\:$</div>\n<p>$$\\begin{cases}<br />\\quad y &=&y_0\\ +\\ v_{0}\\:\\Delta t\\\\\xa0<br /><br />\\quad v &=&v_{0}\\ +\\ \xa0\\frac{F}{m}\\:\\Delta t \\end{cases}$$</p>')
        # Second cell
        cell1 = cell_list[1]
        self.assertIsInstance(cell1, ComputeCell)
        self.assertEqual(cell1.index, 1)
        self.assertEqual(cell1.input, '')
        self.assertEqual(cell1.output, '')
        self.assertEqual(cell1.plain_text_output(), '')

    def test_admin_6(self):
        notebook = NotebookSageNB.find(DOT_SAGE, 'admin:6')
        self.assertEqual(notebook.unique_id, 'admin:6')
        self.assertEqual(notebook.name, 'Test %cython')
        cell_list = list(notebook.cells)
        self.assertEqual(len(cell_list), 2)
        # First cell
        cell0 = cell_list[0]
        self.assertIsInstance(cell0, ComputeCell)
        self.assertEqual(cell0.input, '%hide\n%cython\ncdef str x = "Hello World"\nprint(x)')
        self.assertEqual(cell0.ipython_input(), '%%cython\ncdef str x = "Hello World"\nprint(x)')
