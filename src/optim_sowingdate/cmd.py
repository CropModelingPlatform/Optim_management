from .optimizer import optimize

import os, sys
from pathlib import Path
import click

os.environ["CMD_MODE"] = "1"
__version__ = "1.0.1"

@click.group()
@click.version_option(version=__version__, prog_name="optimal_sowingdate")
def cli():
    pass

@click.command("optim")
@click.argument("modelout")
@click.argument("resultpath")
def cmd_optimize(modelout, resultpath):
    """Optimize sowing date for given model outputs.
    
    modelout: the path of the folder containing the model outputs
    resultpath: the path of the folder where sowing date netcdf files will be saved
    """
    optimize(modelout, resultpath)
cli.add_command(cmd_optimize)

if __name__ == "__main__":
    cli()
