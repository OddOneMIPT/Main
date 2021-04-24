import sys
import argparse
import json
import tempfile
import os

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.exists(storage_path):
    with open(storage_path, 'w') as f: 
        pass
    info_in_data = {}
else:
    with open(storage_path, 'r') as f:
        info_in_data = f.read()
        if len(info_in_data) > 1:
            info_in_data = json.loads(info_in_data)
        else:
            info_in_data = {}


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--key')
    parser.add_argument ('--val')

    return parser


parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
if info_in_data == None:
    if not namespace.val:
        with open(storage_path, 'w') as f:
            f.write(json.dumps({namespace.key: [namespace.val]}))
elif namespace.val:
    if namespace.key in info_in_data:
        info_in_data[namespace.key].append(namespace.val)
        with open(storage_path, 'w') as f:
            f.write(json.dumps(info_in_data))
    else:
        info_in_data[namespace.key] = [namespace.val]
        with open(storage_path, 'w') as f:
            f.write(json.dumps(info_in_data))
else:
    try:
        print(*info_in_data[namespace.key], sep=", ")
    except KeyError:
        print(None)


