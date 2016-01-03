# -*- coding: utf-8 -*-
"""
Jinja2 Environment for Embedded Pages
"""

import os
from jinja2 import Environment, FileSystemLoader


jinja2_env = Environment(
    loader=FileSystemLoader([
        os.path.dirname(__file__)
    ]),
    autoescape=True,
)
