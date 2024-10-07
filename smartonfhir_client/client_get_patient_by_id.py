from fhirclient import client
from fhirclient.models.patient import Patient

def get_patient_by_id():
    settings = {
        'app_id': 'my_web_app',
        'api_base': 'https://r4.smarthealthit.org'
    }
    smart = client.FHIRClient(settings=settings)

    patient = Patient.read('2cda5aad-e409-4070-9a15-e1c35c46ed5a', smart.server)

    if patient:
        print(patient.birthDate.isostring)
        print(smart.human_name(patient.name[0]))
        # '1992-07-03'
        # 'Mr. Geoffrey Abbott'
    else:
        print("Error get patient data.")

if __name__ == '__main__':
    get_patient_by_id()
 
