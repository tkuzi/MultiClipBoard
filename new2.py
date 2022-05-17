import pyperclip
import sys
import json

## access different command line interface
## we save what is put after the python new2.py arg arg arg arg etc in a list
# input = sys.argv[1:]
if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)

    if command == 'save':
        print('save')
    elif command == 'load':
        print('load')
    elif command == 'list':
        print('list')
    else:
        print('unkown command')
else:
    print('please put only one argument')
