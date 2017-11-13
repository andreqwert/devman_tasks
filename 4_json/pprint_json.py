import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding='cp1251') as data_file:
        json_data = json.load(data_file)
        return json_data


def make_json_pretty(json_data):
    json_pretty_data = json.dumps((json_data), ensure_ascii=False, sort_keys=True, indent=4)
    print(json_pretty_data)
    return json_pretty_data


if __name__ == '__main__':
    filepath = input('Enter the path to .json file: ')
    data_loading = load_data(filepath)
    pretty_json = make_json_pretty(data_loading)
