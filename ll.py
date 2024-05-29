import requests

# Your API token
api_token = 'your_api_token_here'

# Base URL for the Deriv API
base_url = 'https://api.deriv.com'

# Endpoint for getting active symbols
endpoint = '/api/v1/active_symbols'

# Full URL
url = f'{base_url}{endpoint}'

# Headers for the request
headers = {
    'Authorization': f'Bearer {api_token}'
}

# Make the request
response = requests.get(url, headers=headers)

# Check the response status
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}, {response.text}')
