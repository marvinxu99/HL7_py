import json
from fhirclient.models.patient import Patient


if __name__ == "__main__":

    #pjs = json.loads('{"id": "patient-1", "name": [{"family": "Parker", "given": ["Peter"]}], "resourceType": "Patient"}')
    pjs = json.loads('{"resourceType": "Patient", "name": [{"family": "Parker", "given": ["Peter"]}]}')
    
    patient = Patient(pjs)
    
    if patient:
        print(patient.name[0].given)
        # ['Peter']
    else:
        print("patient is not correct.")