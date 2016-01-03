## -*- encoding: utf-8 -*-
"""
Handle Command Line Options
"""

import os
import sys
import argparse

from sagenb_export.defaults import DOT_SAGE
from sagenb_export.logger import log
from sagenb_export.sagenb_reader import NotebookSageNB
from sagenb_export.actions import action_list, action_print, action_convert_ipynb


description = \
"""
Export SageNB notebooks
"""


def make_parser():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--log', dest='log', default=None,
                        help='one of [DEBUG, INFO, ERROR, WARNING, CRITICAL]')
    parser.add_argument('--dot-sage', dest='dot_sage', default=DOT_SAGE,
                        help='location of the .sage directory')
    parser.add_argument('--list', dest='list', action='store_true',
                        help='list all SageNB notebooks')
    parser.add_argument('--ipynb', dest='ipynb', default=None,
                        help='output .ipynb notebook filename')
    parser.add_argument('--print', dest='print_text', action='store_true',
                        help='print notebook')
    parser.add_argument('sagenb', default=None, nargs='?',
                        help='SageNB notebook name or unique id')
    return parser

        

def main():
    parser = make_parser()
    args = parser.parse_args()
    if args.log is not None:
        import logging
        level = getattr(logging, args.log)
        log.setLevel(level=level)
    dot_sage = os.path.expanduser(args.dot_sage)
    if args.list:
        action_list(dot_sage)

    if not args.sagenb:
        sys.exit(0)
    sagenb = NotebookSageNB.find(dot_sage, args.sagenb)

    if args.print_text:
        action_print(sagenb)

    if args.ipynb:
        ipynb_name = args.ipynb.format(nb=sagenb)
        if os.path.exists(ipynb_name):
            raise RuntimeError('file exists: {0}'.format(ipynb_name))
        action_convert_ipynb(sagenb, ipynb_name)
    

        
        
