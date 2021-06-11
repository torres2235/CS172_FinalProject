import requests

headers = {"Content-Type": "application/json"}

# Search queries
search = 'http://localhost:9200/test999/_search?pretty'
search_keywords = input("Enter search: ")
search_query = { "query": { "match": {"text": search_keywords}}}

response = requests.get(search, headers=headers, json=search_query)

print(response.status_code)
print(response.text)