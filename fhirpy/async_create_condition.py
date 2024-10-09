import asyncio
# from fhir_client_auto_token import get_fhir_client
from fhir_client import get_fhir_client


async def main():
    client = get_fhir_client()


    # Get the Patient
    patient = await client.resources('Patient').search(_id='f201').get()

    condition = client.resource(
            'Condition',
        id='condition_for_john_thompson',
        code={'coding': [{'system': 'http://snomed.info/sct', 'code': '38341003'}]},
        subject=patient
    )
    
    await condition.save()



if __name__ == '__main__':
    asyncio.run(main())