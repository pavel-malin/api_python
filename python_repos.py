import requests

# Create an API call and save the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Save API response in a variable.
response_dict = r.json()

# Processing results.
print(response_dict.keys())