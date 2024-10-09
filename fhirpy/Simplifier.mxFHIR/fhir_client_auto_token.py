import requests
import time
from fhirpy import AsyncFHIRClient
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

class Config:
    MXFHIR_EMAIL = os.environ.get('MXFHIR_EMAIL')
    MXFHIR_PASSWORD = os.environ.get('MXFHIR_PASSWORD')


# Global variables to store the token and its expiration time
token_info = {
    "token": None,
    "expires_at": None
}

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
        token = data.get('token')  # Extract the token
        expires_in = data.get('expires_in', 36000)  # Assuming expiration is provided, default to 10 hour
        
        # Store token and its expiration time
        token_info['token'] = token
        token_info['expires_at'] = time.time() + expires_in
        
        print(f"New token acquired: {token}")
        return token
    else:
        print(f"Failed to get token. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None


def get_valid_token():
    # Check if the token is valid or expired
    if token_info['token'] is None or token_info['expires_at'] <= time.time():
        # Token is either missing or expired, so fetch a new one
        return get_token()
    else:
        # Return the current valid token
        return token_info['token']


def get_fhir_client():
    """
    This function returns an instance of AsyncFHIRClient with the configuration settings.
    """
    # Get a valid token (either a cached one or a new one if expired)
    token = get_valid_token()
    
    if token:
        # Define the FHIR client (ensure the FHIR server URL is correct)
        client = AsyncFHIRClient(
            url='https://fhir.simplifier.net/mxfhir',
            authorization=f'Bearer {token}',
            extra_headers={
                'Accept': 'application/fhir+json'
            }
        )
        return client
    else:
        print("Failed to get FHIR client due to missing token.")
        return None
