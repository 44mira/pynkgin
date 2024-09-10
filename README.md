# pynkgin

### A GUI program that cycles through a circular buffer of names.

The queue can be moved: 
- forward using the 'NEXT' button or pressing 'Enter' or 'Space' keys.
- back using the 'PREVIOUS' button or pressing 'Backspace' key.

The program can be exited by pressing the 'Q' key.

```
usage: pynkgin.py [-h] [-d DELIMITER] NAMES

positional arguments:
  NAMES                 Path to the file to be read for names.

options:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        The delimiter that separates the names in the file. Defaults to '\n.'
```
