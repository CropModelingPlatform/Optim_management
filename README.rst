Optim Management
================

.. image:: https://readthedocs.org/projects/optim-management/badge/?version=latest
   :target: https://optim-management.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

A package to estimate optimal agricultural practices from crop model outputs.

Installation
------------

**Create a conda environment with Python ≥ 3.9 and install dependencies:**

.. code-block:: bash

   conda create --name gced python=3.9
   pip install optim_management

Usage
-----

It is assumed that you have the NetCDF output files from the models **STICS**, **DSSAT**, and **Celsius** in the same folder, generated using the **LIMA platform**.

We refer to:
- ``ModelOutput`` as the **absolute path** to this folder
- ``resultPath`` as the path where results should be saved

Run the optimization as follows:

.. code-block:: bash

   optim_management optim --start <value> --end <value> --step <value> <ModelOutput> <resultPath>

Contributions
-------------

