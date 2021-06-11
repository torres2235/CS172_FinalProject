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
        index = 'http://localhost:9200/test999/_doc?pretty'

        doc = json.load(f)

        response = requests.post(index, headers=headers, json=doc)

        print(response.status_code)
        print(response.text)

# Search queries
search = 'http://localhost:9200/test999/_search?pretty'
user_input = input("Enter search: ")
search_query = { "query": { "match": {"text": user_input}}}

response2 = requests.get(search, headers=headers, json=search_query)

print(response2.status_code)
print(response2.text)