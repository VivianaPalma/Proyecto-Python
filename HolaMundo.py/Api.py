
import json

import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

payload = {"id": [1, 2, 3, 4, 5, 6], "userId":1}

# A get request to the API
response = requests.get(url, params=payload)

# Print the response
response_json = response.json()

print(json.dumps(response_json, indent=5))

print(response)


