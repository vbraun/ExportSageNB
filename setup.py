#!/usr/bin/env python

from distutils.core import setup

setup(
    name='sagenb_export',
    description='Export Notebooks from SageNB',
    author='Volker Braun',
    author_email='vbraun.name@gmail.com',
    install_requires=[
        'ipython>=4',
        'nbconvert>=4',
    ],
    packages=['sagenb_export'],
    entry_points={
        'console_scripts': [
            'sagenb-export = sagenb_export.cmdline:main',
        ],
    },
    version='1.0',
    url='https://github.com/sagemath/sagenb-export',
)
