Usage
=====


It is assumed that you have the NetCDF output files from the models **STICS**, **DSSAT**, and **Celsius** in the same folder, generated using the **LIMA platform**.

We refer to:
- ``ModelOutput`` as the **absolute path** to this folder
- ``resultPath`` as the path where results should be saved

Run the optimization as follows:

.. code-block:: bash

   optim_management optim --start <value> --end <value> --step <value> <ModelOutput> <resultPath>
