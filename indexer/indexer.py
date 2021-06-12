import requests
import os
import json

headers = {"Content-Type": "application/json"}

# Retrieve the names of all files to be indexed in folder ./ap89_collection_small of the current directory
for dir_path, dir_names, file_names in os.walk("docs"):
    allfiles = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]

# Index all of our docs
for file in allfiles:
    with open(file, 'r') as f:
        index = 'http://localhost:9200/croogler_index/_doc?pretty'

        doc = json.load(f)

        response = requests.post(index, headers=headers, json=doc)

        print(response.status_code)
        print(response.text)