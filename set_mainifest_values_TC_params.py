import argparse
import json

def open_manifest(file_location):
    with open(file_location, 'r') as f:
        data = json.load(f)
    return data

def get_manifest_values(file_location, keys):
    manifest = open_manifest(file_location)
    values = {}
    for key in keys:
        values[key] = manifest.get(key)
    return values

def set_teamcity_params(values):
    for key, value in values.items():
        if key == "sa_version":
            key = "version"
        print("##teamcity[setParameter name='{}' value='{}']".format(key, value))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read values from a JSON manifest file')
    parser.add_argument('file_location', type=str, help='Location of the JSON manifest file')
    parser.add_argument('keys', type=str, nargs='+', help='List of keys to retrieve from the manifest')
    args = parser.parse_args()
    
    file_location = args.file_location
    keys = args.keys
    values = get_manifest_values(file_location, keys)
    set_teamcity_params(values)
