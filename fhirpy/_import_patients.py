import os  
import asyncio
import fhirpy

from initialize import import_dataset, import_bundle
from fhir_client import get_fhir_client


async def import_patients():
    
    client = get_fhir_client()

    dataset_path = '''D:/dDev/Python/__HL7_py/fhirpy/dataset'''

    try:
        # await import_dataset(client, dataset_path)
        await import_bundle(client, dataset_path+'/patient-1.json')

    except Exception as e:
        print(f"Exception details: {str(e)}")

    resources = client.resources('Patient')
    print(await resources.count())


if __name__ == '__main__':
    asyncio.run(import_patients())