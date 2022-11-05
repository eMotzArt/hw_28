from pathlib import Path
import csv
import json

FOLDER_NAME = 'datasets'

PATH = Path(__file__).parent.absolute().joinpath(FOLDER_NAME)
FILES_PATH = list(PATH.iterdir())

def csv_to_json(csv_file_path, json_file_path):
    json_array = []

    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            json_array.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_string = json.dumps(json_array, indent=4, ensure_ascii=False)
        # some correction for all-to-one format
        json_string = json_string.replace('"TRUE"', '"True"').replace('"FALSE"', '"False"').replace('"Id"', '"id"')
        json_file.write(json_string)

def compile_jsons():
    for file in FILES_PATH:
        csv_to_json(file, file.with_suffix('.json'))