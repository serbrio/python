import os
import tempfile
import argparse
import json
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument('--key', help='--key <key_name>')
parser.add_argument('--val', help='--val <value>')
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


#def opnjs():
#    with open(storage_path, 'rw') as f:
#        stor = json.load(f)


def main():
    if args.key and args.val:
        with open(storage_path, 'r') as f:
            oD = OrderedDict()
            try:
                oD = json.load(f)
            except:
                print('load json except')
            if args.key in oD:
                oD[args.key].append(args.val)
            else:
                oD[args.key] = [args.val]
            with open(storage_path, 'w') as final:
                json.dump(oD, final)
                print('key and val written')

    elif args.key:
        with open(storage_path, 'r') as f:
            oD = OrderedDict()
            try:
                oD = json.load(f)
            except:
                print('load json except (key branch)')
            if args.key in oD:
                print(', '.join(oD[args.key]))
                print('key in the list')
            else:
                print(None)


if __name__ == '__main__':
    main()