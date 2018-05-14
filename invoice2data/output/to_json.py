import json


def write_to_file(data, path):
    if path.endswith('.json'):
        filename = path
    else:
        filename = path + '.json'

    with open(filename, "w") as json_file:
        for line in data:
            line['date'] = line['date'].strftime('%d/%m/%Y')
        json.dump(data, json_file, indent=4,  sort_keys=True)
