#!/usr/bin/env python3

import tkinter
from tkinter import ttk
import argparse
from pathlib import Path
from textwrap import dedent

# [[ Command line flags ]] {{{

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=dedent(
        """
        A GUI program that cycles through a circular buffer of names.

        The queue can be moved: 
        - forward using the 'NEXT' button or pressing 'Enter' or 'Space' keys.
        - back using the 'PREVIOUS' button or pressing 'Backspace' key.

        The program can be exited by pressing the 'Q' key.
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
NAMES, DELIMITER = Path(args.names), args.delimiter

if not NAMES.exists():
    raise FileNotFoundError("File does not exist at the specified path.")

# }}}

# [[ GUI Initialization ]] {{{1

root = tkinter.Tk()
root.title(f"pynkgin: {NAMES}")
root.resizable(False, False)

# [[ Style Definitions ]] {{{2

style = ttk.Style()

# Button with conditional rendering
style.configure(
    "TButton",
    font="Arial 36",
    relief="flat",
    borderwidth=3,
    padding=16,
    background="#c5b4ac",
    foreground="#070605",
)

style.map(
    "TButton",
    background=[
        ("active", "!pressed", "#7ba392"),
        ("pressed", "!disabled", "#415e42"),
    ],
    foreground=[("active", "#f0ecea")],
)

# Text frame
style.configure(
    "TLabel",
    font="Arial 72",
    background="#27221A",
    foreground="#f0ecea",
)

# Frame
style.configure(
    "TFrame",
    background="#27221A",
)

# }}}2

frame = ttk.Frame()

# Create button and apply style
button_next = ttk.Button(
    frame,
    text="NEXT",
)

button_prev = ttk.Button(
    frame,
    text="PREVIOUS",
)

button_next.pack(side="right", padx=25)
button_prev.pack(side="left", padx=25)

name = tkinter.StringVar()
name.set("START")
label = ttk.Label(root, textvariable=name)


label.pack(expand=1, padx=50, pady=75)
frame.pack(expand=1, side="bottom", pady=50)

# }}}1

# Close program on Q press
root.bind("<Key-q>", lambda _: root.destroy())

# }}}1

root.mainloop()
