from fhirclient.models.patient import Patient
from fhirclient.models.humanname import HumanName


if __name__ == "__main__":
    patient = Patient({'id': 'patient-1'})
    print(patient.id)
    # patient-1

    name = HumanName()
    name.given = ['Peter']
    name.family = 'Parker'
    patient.name = [name]
    print(patient.as_json())
    # {'id': 'patient-1', 'name': [{'family': 'Parker', 'given': ['Peter']}], 'resourceType': 'Patient'}

    name.given = 'Peter'
    print(patient.as_json())
    # throws FHIRValidationError:
    # {root}:
    #   name.0:
    #     given:
    #       Expecting property "given" on <class 'fhirclient.models.humanname.HumanName'> to be list, but is <class 'str'>
