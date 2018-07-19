import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--key', help='--key <key_name>')
parser.add_argument('--val', help='--val <value>')
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def storage_dict():
    d = {}
    try:
        with open(storage_path, 'r') as f:
            try:
                d = json.load(f)
            except:
                pass
        return d
    except:
        with open(storage_path, 'w') as f:
            return d


def main():
    if args.key and args.val:
        stor = storage_dict()
        if args.key in stor:
            stor[args.key].append(args.val)
        else:
            stor[args.key] = [args.val]
        with open(storage_path, 'w') as final:
            json.dump(stor, final)
    elif args.key:
        stor = storage_dict()
        if args.key in stor:
            print(', '.join(stor[args.key]))
        else:
            print(None)


if __name__ == '__main__':
    main()