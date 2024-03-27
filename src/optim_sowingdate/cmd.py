from .optimizer import optimize

import os, sys
from pathlib import Path
import click

os.environ["CMD_MODE"] = "1"
__version__ = "2.0.11"

@click.group()
@click.version_option(version=__version__, prog_name="optimal_sowingdate")
def cli():
    pass

@click.command("optim")
@click.argument("modelout")
@click.argument("prefix")
def cmd_optimize(modelout, prefix):
    """Optimize sowing date for given model outputs.

    
    modelout: the folder containing the model outputs
    prefix: the prefix for the output file
    """
    optimize(modelout, prefix)

cli.add_command(cmd_optimize)

if __name__ == "__main__":
    cli()
