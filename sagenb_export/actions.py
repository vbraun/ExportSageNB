
import sys
from sagenb_export.logger import log
from sagenb_export.sagenb_reader import NotebookSageNB


def action_list(dot_sage):
    def tr(unique_id, name):
        print('{0:<15} | {1}'.format(unique_id, name))
    tr('Unique ID', 'Notebook Name')
    print('-' * 79)
    notebooks = dict(
        (notebook.sort_key, notebook)
        for notebook in NotebookSageNB.all_iter(dot_sage)
    )
    for key in sorted(notebooks.keys()):
        notebook = notebooks[key]
        tr(notebook.unique_id, notebook.name)



def action_print(sagenb):
    from sagenb_export.text_writer import TextWriter
    TextWriter(sagenb).write(sys.stdout)


def action_convert_ipynb(sagenb, ipynb_filename):
    from sagenb_export.ipynb_writer import IpynbWriter
    IpynbWriter(sagenb).write(ipynb_filename)
