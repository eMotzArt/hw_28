import csv
import json

def load_csv_as_json(csv_file_path):
    json_array = []

    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            json_array.append(row)

    json_string = json.dumps(json_array, indent=4, ensure_ascii=False)
    # some correction for all-to-one format
    json_string = json_string.replace('"TRUE"', '"True"').replace('"FALSE"', '"False"').replace('"Id"', '"id"')
    return json.loads(json_string)
