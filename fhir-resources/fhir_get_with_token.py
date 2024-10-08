import requests
from fhir.resources.patient import Patient


if __name__ == '__main__':

    # The Bearer token
    token = "YOUR_ACCESS_TOKEN"

    # The URL you are sending the request to
    url = "https://fhir.simplifier.net/mxfhir/Patient/f201"

    # Set up the headers, including the Bearer token in the Authorization header
    headers = {
        "Authorization": f"Bearer {token}",
        'Accept': 'application/fhir+json'
    }

    # Send a GET request with the headers
    response = requests.get(url, headers=headers)

    # Print the response
    print(response.status_code)
    print(response.json())  # If the response contains JSON data

    patient = Patient.parse_raw(response.text)

    print(patient.json())
    print(patient.name[0].use, patient.name[0].given[0], patient.name[0].family)