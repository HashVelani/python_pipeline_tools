import json
import argparse

def open_manifest(file_location):
    with open(file_location, 'r') as f:
        data = json.load(f)
    return data

def set_teamcity_params(values):
    for key, value in values.items():
        if key == "sa_version":
            print("##teamcity[setParameter name='sa_version' value='{}']".format(values["version"]))
        else:
            print("##teamcity[setParameter name='{}' value='{}']".format(key, value))

def get_manifest_values(file_location, keys):
    manifest = open_manifest(file_location)
    values = {}
    for key in keys:
        values[key] = manifest[key]
    return values

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read values from a JSON manifest file')
    parser.add_argument('file_location', type=str, help='Location of the JSON manifest file')
    parser.add_argument('keys', type=str, nargs='+', help='List of keys to retrieve from the manifest')
    args = parser.parse_args()
    
    file_location = args.file_location
    keys = args.keys
    values = get_manifest_values(file_location, keys)
    set_teamcity_params(values)
