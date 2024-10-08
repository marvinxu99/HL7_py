import requests
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

class Config:
    MXFHIR_EMAIL = os.environ.get('MXFHIR_EMAIL')
    MXFHIR_PASSWORD = os.environ.get('MXFHIR_PASSWORD')


def get_token():
    url = "https://api.simplifier.net/token"
    
    # Request payload (body)
    payload = {
        "Email": Config.MXFHIR_EMAIL,
        "Password": Config.MXFHIR_PASSWORD
    }
    
    # Perform a POST request
    response = requests.post(url, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the response as JSON
        print(data)
        token = data.get('token')  # Extract the token from the response
        expires_in = data.get('expires_in', 3600)
        print(f"Token: {token}")
        print(expires_in)
    else:
        print(f"Failed to get token. Status code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == '__main__':
    get_token()