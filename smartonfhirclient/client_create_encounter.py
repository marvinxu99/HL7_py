import json
from fhirclient import client
from fhirclient.models.encounter import Encounter

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWFydmlueHUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ4MTk4YWUwLWY2ZWItNDE3MC1iOTRmLWRmNTFjMzAwNTc2NyIsImp0aSI6ImEyMzIzMzU3LTRlMWEtNDg1ZS05YTU3LTZjMjllNzIyODIzNiIsImV4cCI6MTcyODI4OTg3MSwiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.o1nZYsXEdDa2Uv0wel0xiS6Tx5j_6jH5xGeNZvd5h8E"

settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://r4.smarthealthit.org',   #'https://fhir.simplifier.net/mxfhir',
}

def create_encounter():

    smart = client.FHIRClient(settings=settings)

    enc_data = {
       "resourceType": "Encounter",
        "text": {
            "status": "generated",
            "div": "<div>Encounter with patient @example</div>"
        },
        "status": "in-progress",
        "class": {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": "IMP",
            "display": "inpatient encounter"
        },
        "subject": {
            "reference": "Patient/example"
        },
    }

    #enc_json = json.loads(data_json)

    # Create an Encounter instance with the encounter data
    encounter = Encounter(enc_data)
    response = encounter.create(smart.server)

    if response:
        print(f"Encounter created with ID: {response['id']}")
        print(response)
    else:
        print("Error in creating encounter.")


if __name__ == '__main__':
    create_encounter()





