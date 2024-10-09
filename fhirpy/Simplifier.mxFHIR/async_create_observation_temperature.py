import asyncio
# from fhir_client_auto_token import get_fhir_client
from fhir_client import get_fhir_client


async def main():

    client = get_fhir_client()

    # For temperature 
    observation = client.resource(
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
                'code': '8310-5'                
            }]
        }
    )

    # 8310-5 for body temperature  - 96.8 degF
    observation['effectiveDateTime'] = '2018-10-20'
    observation['valueQuantity'] = {
        'system': 'http://unitsofmeasure.org',
        'value': 96.8,
        'code': 'degF'
    }

    # Connect the Observation to the Patient
    patient = await client.resources('Patient').search(_id='f201').get()
    observation['subject'] = patient.to_reference()                        # Patient reference is stored in Observation.subject.

    await observation.save()


if __name__ == '__main__':
    asyncio.run(main())