import requests
from fhir.resources.patient import Patient

def test():

    # Make an API request to get a patient resource
    response = requests.get('https://fhir.simplifier.net/mxfhir/Patient/f201')

    print(response.json())

    # Parse the FHIR resource
    patient = Patient.parse_raw(response.text)

    # Access data
    print(patient.name[0].family)


if __name__ == "__main__":
    test()