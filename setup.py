#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='sagenb_export',
    description='Export Notebooks from SageNB',
    author='Volker Braun',
    author_email='vbraun.name@gmail.com',
    install_requires=[
        'six',
        'ipython>=4',
        'nbconvert>=4',
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'sagenb-export = sagenb_export.cmdline:main',
        ],
    },
    version='2.0',
    url='https://github.com/vbraun/ExportSageNB',
)
