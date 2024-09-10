#!/usr/bin/env python3

import tkinter
from tkinter import ttk
import argparse
from textwrap import dedent

import sv_ttk

# [[ Command line flags ]] {{{

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=dedent(
        """
        A GUI program that cycles through a circular buffer of names.

        The queue can be advanced using the 'NEXT' button or pressing 'Enter' or 'Space' keys.
        The program can be closed by pressing the 'Q' key.
        """
    ),
    epilog="github.com/44mira/pynkgin",
)

# Definitions
parser.add_argument(
    "names",
    metavar="NAMES",
    help="Path to the file to be read for names.",
)
parser.add_argument(
    "-d",
    "--delimiter",
    metavar="DELIMITER",
    default="\n",
    help="The delimiter that separates the names in the file. Defaults to '\\n.'",
)

# Read input flags
args = parser.parse_args()
NAMES, DELIMITER = args.names, args.delimiter

# }}}
