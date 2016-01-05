

from nbformat import write
from nbformat.v4 import (
    new_code_cell, new_markdown_cell,
    new_notebook,
    new_output
)
from nbformat.v4.nbbase import new_raw_cell


from sagenb_export.logger import log
from sagenb_export.sagenb_reader import TextCell, ComputeCell


class IpynbWriter(object):

    def __init__(self, sagenb):
        self.nb = sagenb

        
    @property
    def cells(self):
        for cell in self.nb.cells:
            if isinstance(cell, TextCell):
                yield new_markdown_cell(
                    source=cell.input,
                )
            elif isinstance(cell, ComputeCell):
                yield new_code_cell(
                    source=cell.input,
                    execution_count=cell.index,
                    outputs=[
                        new_output(
                            output_type=u'execute_result',
                            data={
                                'text/plain': cell.output,
                            },
                            execution_count=cell.index,
                        )
                    ]
                )
            else:
                log.critical('unknown cell: {0}'.format(cell))

        
    def write(self, filename):
        ipynb = new_notebook(
            cells=list(self.cells),
            metadata=dict(
                kernelspec=dict(
                    display_name="SageMath",
                    name="sagemath",
                ),
                language='python',
            )
        )
        write(ipynb, filename)
        
