Convert SageNB Notebooks
========================

This is a tool to convert SageNB notebooks to other formats, in
particular IPython/Jupyter notebooks.


Install
-------

    pip install 


Usage
-----

First, you want to list the existing notebooks. Each notebook has a
unique id and a not necessarily unique name:

    $ sagenb-export --list
    Unique ID       | Notebook Name
    -------------------------------------------------------------------------------
    admin:10        | Oxford Seminar (1,1)-Calabi Yau

You can specify notebooks by the ID or by name; If the name is not
unique, the first notebook found in the filesystem wins. To convert it
to a Jupyter/IPython notebook, use the `--ipynb` switch as in

    $ sagenb-export --ipynb=Output.ipynb admin:10

You can then open the saved `Output.ipynb` via

    $ sage --notebook=jupyter Output.ipynb


Notes
-----

* Various output formats are not supported, e.g. no pictures. The
  simplest solution is to re-evaluate.

* SageNB html input cells are converted to Jupyter raw NBConvert
  cells; In the interactive Jupyter notebook these are not rendered as
  html but shown as their html source code. If you export to HTML
  (File -> Download as -> HTML) they are rendered as html, though.

