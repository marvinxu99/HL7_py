import asyncio
# from fhir_client_auto_token import get_fhir_client
from fhir_client import get_fhir_client


async def main():
    client = get_fhir_client()

    weight_observation = client.resource(
        'Observation',
        status='preliminary',
        category=[{
            'coding': [{
                'system': 'http://hl7.org/fhir/observation-category',
                'code': 'vital-signs'
            }]
        }],
        code={
            'coding': [{
                'system': 'http://loinc.org',
                'code': '3141-9'
            }]
        },
        effectiveDateTime='2018-10-20',
        valueQuantity={
            'system': 'http://unitsofmeasure.org',
            'value': 85,
            'code': 'kg'
        }
    )

    # Connect the Observation to the Patient
    patient = await client.resources('Patient').search(_id='f201').get()
    weight_observation['subject'] = patient.to_reference()                        # Patient reference is stored in Observation.subject.

    await weight_observation.save()

    # SBP & DBP
    blood_pressure_observation = client.resource(
        'Observation',
        status='preliminary',
        category=[{
            'coding': [{
                'system': 'http://hl7.org/fhir/observation-category',
                'code': 'vital-signs'
            }]
        }],
        code={
            'coding': [{
                'system': 'http://loinc.org',
                'code': '55284-4'                   # section header code for BP is 55284-4
            }]
        },
        component=[
            {
                'code': {
                    'coding': [{
                        'system': 'http://loinc.org',
                        'code': '8480-6'
                    }]
                },
                'valueQuantity': {
                    'system': 'http://unitsofmeasure.org',
                    'value': 140,
                    'code': 'mmHg'
                }
            },
            {
                'code': {
                    'coding': [{
                        'system': 'http://loinc.org',
                        'code': '8462-4'
                    }]
                },
                'valueQuantity': {
                    'system': 'http://unitsofmeasure.org',
                    'value': 90,
                    'code': 'mmHg'
                }
            }
        ],
        effectiveDateTime='2018-10-20',
        subject=patient.to_reference()
    )

    await blood_pressure_observation.save()

    

if __name__ == '__main__':
    asyncio.run(main())