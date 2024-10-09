import json
import asyncio

from fhir_client import get_fhir_client


async def main():
    
    client = get_fhir_client()

    filename = 'D:/dDev/Python/__HL7_py/fhirpy/dataset/initial_data.json'

    try:
        with open(filename) as fd:
            data_json = json.load(fd)

            for entry in data_json['entry']:
                print(entry['resource']['resourceType'])
                data = entry['resource']
                await client.resource(entry['resource']['resourceType'], **data).save()

    except Exception as e:
        print(f"Exception details: {str(e)}")


if __name__ == '__main__':
    asyncio.run(main())