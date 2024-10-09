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
        effectiveDateTime='2018-10-22',
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

    print(weight_observation)

    

if __name__ == '__main__':
    asyncio.run(main())