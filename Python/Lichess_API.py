import requests
token = "insert_api_token_here"  # Replace with your Lichess API token

#Gather Player Information

"""
def get_my_profile(token):
    url = "https://lichess.org/api/account"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
# Replace 'YOUR_PERSONAL_ACCESS_TOKEN' with your actual Lichess API token
token = "insert_api_token_here"  # Replace with your Lichess API token
profile_data = get_my_profile(token)
if profile_data:
    print(profile_data)
else:
    print("Failed to retrieve profile data.")
"""

#Get My Games

"""
import requests

def get_my_games(token, username, max_games=10):
    url = f"https://lichess.org/api/games/user/{username}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "max": max_games,
        "pgnInJson": True
    }

    response = requests.get(url, headers=headers, params=params)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return None
    else:
        return None

# Replace 'YOUR_USERNAME' with your actual Lichess username
username = "TrickyPot1"
token = "insert_api_token_here"  # Replace with your Lichess API token
games_data = get_my_games(token, username)

if games_data:
    print(games_data)
else:
    print("Failed to retrieve games data.")
"""

"""
#Download someone's Games

# Replace with your Lichess username and API token
username = 'TrickyPot1'
token = 'lip_ioAm09bwwv9HqMpkxwCe'

# Set the headers with your API token
headers = {
    'Authorization': f'Bearer {token}'
}

# Define the endpoint and parameters
endpoint = f'https://lichess.org/api/games/user/{username}'
params = {
    'max': 10000,  # Adjust the number of games you want to fetch
    'clocks': 'false',  # Include clock information
    'evals': 'false',  # Include evaluation data
    'opening': 'false',  # Include opening data
    'perfType': 'rapid',  # Filter by game type (e.g., blitz, rapid, etc.)
    'pgnInJson': 'true'  # This will be ignored since we expect plain PGN
}

# Make the API request
response = requests.get(endpoint, headers=headers, params=params)

# Print the response content for debugging
print("Response status code:", response.status_code)
print("Response content:", response.content.decode('utf-8'))
random_counter = random.randint(1, 1000000000)
if response.status_code == 200:
    # Save the response content directly to a PGN file
    with open(f'/Users/neevgrover/Documents/Python Programs/Lichess_Downloads/games{random_counter}.pgn', 'w') as file:
        file.write(response.content.decode('utf-8'))

    print("Games exported successfully!")
else:
    print(f"Error fetching games: {response.status_code}")
"""

#Create a Study

import requests

# Replace with your actual Lichess API token
API_TOKEN = 'insert_api_token_here'  # Replace with your Lichess API token

# Headers with authorization
headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}

# Study creation endpoint
url = 'https://lichess.org/api/studies'

# Data for the study
data = {
    'name': 'My New Study',  # The name of your study
    'description': 'A study created via the Lichess API',  # Description of the study
    'chapterName': 'Chapter 1',  # Name of the first chapter
    'public': True,  # Whether the study is public
    'inviteOnly': False  # Whether the study is invite-only
}

# Making the POST request to create the study
response = requests.post(url, headers=headers, json=data)

# Checking if the request was successful
if response.status_code == 200:
    print("Study created successfully!")
    print("Study URL:", response.json()['url'])
else:
    print("Failed to create study.")
    print("Response:", response.json())