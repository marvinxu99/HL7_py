import requests

def get_token():
    url = "https://api.simplifier.net/token"
    
    # Request payload (body)
    payload = {
        "Email": "marvinxu99@hotmail.com",
        "Password": "weTobin010525"
    }
    
    # Perform a POST request
    response = requests.post(url, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the response as JSON
        # print(data)
        token = data.get('token')  # Extract the token from the response
        print(f"Token: {token}")
    else:
        print(f"Failed to get token. Status code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == '__main__':
    get_token()