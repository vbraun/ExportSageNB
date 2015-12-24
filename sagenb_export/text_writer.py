
from sagenb_export.logger import log
from sagenb_export.sagenb_reader import TextCell, ComputeCell


HEADER = """
Name: {nb.name}
"""

TEXT_CELL = """
Text: {cell.input}
"""


COMPUTE_CELL = """
In[{cell.index}]: {cell.input}
Out[{cell.index}]: {cell.output}
"""


class TextWriter(object):

    def __init__(self, sagenb):
        self.nb = sagenb

    @property
    def header(self):
        return HEADER.format(nb=self.nb)

    @property
    def cells(self):
        for cell in self.nb.cells:
            if isinstance(cell, TextCell):
                yield TEXT_CELL.format(cell=cell)
            elif isinstance(cell, ComputeCell):
                yield COMPUTE_CELL.format(cell=cell)
            else:
                log.critical('unknown cell: {0}'.format(cell))
    
    def write(self, stream):
        stream.write(self.header)
        for cell in self.cells:
            stream.write(cell)
    
