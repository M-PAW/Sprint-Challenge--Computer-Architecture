

"""
Main File
"""

import sys
from cpu import *

if len(sys.argv) == 2:
    filename= sys.argv[1]
    cpu = CPU()
    cpu.load(filename)
    cpu.run()
else:
    print('Error: please enter a valid file name to continue.');
    sys.exit(1)