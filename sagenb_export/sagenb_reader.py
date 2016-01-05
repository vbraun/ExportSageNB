
import os
import re
import cPickle

from sagenb_export.logger import log



CELL_FRONT = re.compile(u'^\{\{\{id=(?P<index>[0-9]*)\|$')
CELL_MID = re.compile(u'^///$')
CELL_BACK = re.compile(u'^\}\}\}$')



class Cell(object):

    def __init__(self, input):
        self.input = input

    def __repr__(self):
        return '{0}:"{1}"'.format(type(self), self.input)

class ComputeCell(Cell):

    def __init__(self, index, input, output):
        assert index >= 0
        super(ComputeCell, self).__init__(input)
        self.index = index
        self.output = output
    

class TextCell(Cell):
    pass
    


class WorksheetParser(object):

    def __init__(self, worksheet_html):
        self.worksheet_lines = worksheet_html.splitlines()
        self.pos = 0
        self.index = -1
        log.debug('Worksheet has %s lines', len(self.worksheet_lines))
        
    @property
    def line(self):
        return self.worksheet_lines[self.pos]

    def get_line_and_forward(self):
        line = self.line
        self.pos += 1
        return line

    @property
    def is_finished(self):
        return self.pos >= len(self.worksheet_lines)

    @property
    def is_cell_front(self):
        match = CELL_FRONT.match(self.line)
        if match:
            self.index = int(match.group('index'))
            return True
        else:
            return False

    @property
    def is_cell_mid(self):
        match = CELL_MID.match(self.line)
        return match != None

    @property
    def is_cell_back(self):
        match = CELL_BACK.match(self.line)
        return match != None

    def _try_read_text(self):
        accumulator = []
        while not (self.is_cell_front or self.is_finished):
            log.debug('Read text: %s', self.line)
            accumulator.append(self.get_line_and_forward())
        accumulator = u'\n'.join(accumulator).strip()
        if accumulator:
            return TextCell(accumulator)

    def _read_cell_input(self):
        assert self.is_cell_front
        self.pos += 1
        accumulator = []
        while not (self.is_cell_mid or self.is_finished):
            log.debug('Read cell input: %s', self.line)
            accumulator.append(self.get_line_and_forward())
        return u'\n'.join(accumulator).strip()

    def _read_cell_output(self):
        assert self.is_cell_mid
        self.pos += 1
        accumulator = []
        while not (self.is_cell_back or self.is_finished):
            log.debug('Read cell output: %s', self.line)
            accumulator.append(self.get_line_and_forward())
        return u'\n'.join(accumulator).strip()

    def _read_cell(self):
        input = self._read_cell_input()
        output = self._read_cell_output()
        return ComputeCell(self.index, input, output)
        
    def __iter__(self):
        while not self.is_finished:
            text = self._try_read_text()
            if text:
                yield text
            yield self._read_cell()
            if not self.is_finished:
                assert self.is_cell_back
                self.pos += 1
        


class NotebookSageNB(object):

    def __init__(self, path):
        log.debug('opening notebook root directory: %s', path)
        self.path = path
        with open(os.path.join(path, 'worksheet.html'), 'rb') as f:
            self.ws = f.read().decode('utf-8')
        with open(os.path.join(path, 'worksheet_conf.pickle')) as f:
            self.conf = cPickle.load(f)

    def __repr__(self):
        return '{0}:"{1}"'.format(self.unique_id, self.name)
            
    @classmethod
    def all_iter(cls, dot_sage):
        store = os.path.join(dot_sage, 'sage_notebook.sagenb', 'home', '__store__')
        for path, dirs, files in os.walk(store):
            worksheet = os.path.join(path, 'worksheet.html')
            if os.path.isfile(worksheet):
                yield cls(path)

    @classmethod
    def find(cls, dot_sage, name_or_unique_id):
        for notebook in cls.all_iter(dot_sage):
            if notebook.unique_id == name_or_unique_id:
                return notebook
            if notebook.name == name_or_unique_id:
                return notebook
        raise ValueError('no such notebook: {0}'.format(name_or_unique_id))
                
    @property
    def sort_key(self):
        return (self.conf['owner'], self.conf['id_number'])
            
    @property
    def unique_id(self):
        return '{0}:{1}'.format(self.conf['owner'], self.conf['id_number'])

    @property
    def name(self):
        return self.conf['name']

    @property
    def cells(self):
        for cell in WorksheetParser(self.ws):
            log.debug('Cell: %s', cell)
            yield cell
            
