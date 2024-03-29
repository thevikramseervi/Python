# Ending a program early with sys.exit()

import sys
while True:
    r = input("Type exit to stop the program: ")
    if r == 'exit':
        sys.exit()