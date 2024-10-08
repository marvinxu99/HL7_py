import asyncio
from fhirpy import AsyncFHIRClient


async def main():
    # Create an instance
    client = AsyncFHIRClient(
        'https://fhir.simplifier.net/mxfhir',
        None,
        {
            'Accept': 'application/fhir+json'
        }
        # authorization='Bearer TOKEN',
    )

    # Search for patients
    resources = client.resources('Patient')  # Return lazy search set
    

    # Getting multiple patients
    patients = await resources.fetch()  # Returns list of AsyncFHIRResource
    for pt in patients:
        # print(pt.serialize())
        print(
            "ID: ", pt['id'],
            "\n Name:", pt['name'][0]['given'][0], pt.get_by_path('name.0.family') 
        )

    print("=======================")

    # Search Patients
    # patients = await client.resources('Patient').search(name=['Wesley9', 'Xu']).fetch_all()
    patients = await client.resources('Patient').search(gender='male').fetch_all()  # OR
    for pt in patients:
        print(pt.serialize())
        print(
            "ID: ", pt['id'],
            "\n Name:", pt['name'][0]['given'][0], pt.get_by_path('name.0.family') 
        )

    print("=======================")

    # Only get one patient
    resources = resources.search(_id='f201')
    patient = await resources.get()  # return one patient
    print(patient.serialize())

    print(
        "ID: ", patient.get('id'), ", "
        "Name:", patient.get_by_path('name.0.given.0'), patient['name'][0]['family']
    )

     


if __name__ == '__main__':
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    asyncio.run(main())