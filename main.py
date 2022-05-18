from re import S
import pyperclip
import sys
import json
import clipboard

SAVED_DATA = "clipboard.json"

## access different command line interface
## we save what is put after the python new2.py arg arg arg arg etc in a list
# input = sys.argv[1:]
def save_data(filepath, data):
    #write : maak aan als het niet bestaat of overwrite als die er al is
    with open(filepath, 'w') as f:
        json.dump(data, f, indent= 2)

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        ## als de file niet bestaat returnen we een lege dictionary
        return {}



if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input('please provide a key:  ')
        data[key] = pyperclip.paste()
        save_data(SAVED_DATA, data)
        print('data saved')

    elif command == 'load':
        key= input('please provide the loaded key:  ')
        if key in data:
            pyperclip.copy(data[key])
            print(data[key])
            print('data copied')
        else:
            print('data key does not exist')

    elif command == 'list':
        for i,y in enumerate(data):
            print(str(i) +   '    ' + str(y) + '    ' + str(data[y]))
    else:
        print('unkown command')
else:
    print('please put only one argument')


