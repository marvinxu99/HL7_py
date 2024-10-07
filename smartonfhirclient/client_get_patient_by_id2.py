from fhirclient import client
from fhirclient.models.patient import Patient

token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWFydmlueHUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ4MTk4YWUwLWY2ZWItNDE3MC1iOTRmLWRmNTFjMzAwNTc2NyIsImp0aSI6ImE0YmRlODY0LTkwYTAtNDdlNi05NzczLTAzNDdjOTRiNjE2NCIsImV4cCI6MTcyODI2OTYyMywiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.wNccto2gIL73B56xEdN2kUCTYy5-NVQo9bnvCVXlFi8"

settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://fhir.simplifier.net/mxfhir',
    'launch_tocken': f'Bearer {token}'
}

def get_patient_by_id():

    smart = client.FHIRClient(settings=settings)

    patient = Patient.read('f201', smart.server)

    if patient:
        print(patient.gender)
        print(smart.human_name(patient.name[0]))
        # '1992-07-03'
        # 'Mr. Geoffrey Abbott'
    else:
        print("Error get patient data.")

if __name__ == '__main__':
    get_patient_by_id()





