import os
from contextlib import suppress


with suppress(OSError):
    os.remove('somefile.txt')