#!/usr/bin/env python3

import tkinter
from tkinter import ttk
import argparse

import sv_ttk

# [[ Command line flags ]] {{{

parser = argparse.ArgumentParser(
    description="A GUI program that cycles through a circular buffer of names.",
    epilog="github.com/44mira/pynkgin",
)

# Definitions
parser.add_argument(
    "names",
    metavar="NAMES",
    help="The file to be read for names.",
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
