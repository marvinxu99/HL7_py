import asyncio
from fhirpy import AsyncFHIRClient


# Example of feteching encounters without include
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

    # Search for encounters
    resources = client.resources('Encounter')  # Return lazy search set
    # By patient
    resources = resources.search(subject='Patient/example1').limit(10)
    # by id
    # resources = resources.search(_id='example2').limit(10)
    encounters = await resources.fetch() # Returns list of AsyncFHIRResource

    print("Number of encounters found: ", len(encounters))
    # print(encounters[0]['id'])
    
    for enc in encounters:
        print("Encounter ID: ", enc.id)
            # Check if the 'location' field exists in the encounter resource
        if 'location' in enc and len(enc['location']) > 0:
            location_ref = enc['location'][0]['location']['reference']
            location_display = enc['location'][0]['location'].get('display', 'n/a')
            print(f"Location Reference: {location_ref}, Location Display: {location_display}")
        else:
            print("Location details not available.")


# Example of fetching with include
async def main_with_include():
    # Create an instance
    client = AsyncFHIRClient(
        'https://fhir.simplifier.net/mxfhir',
        None,
        {
            'Accept': 'application/fhir+json'
        }
        # authorization='Bearer TOKEN',
    )

    # Search for encounters
    resources = client.resources('Encounter')  # Return lazy search set
    # By patient
    resources = resources.search(subject='Patient/example1').limit(10)
    # by id
    # resources = resources.search(_id='example2').limit(10)
    result = await resources.include('Encounter', 'patient', 'location').fetch_raw()

    for entry in result.entry:
        print(entry.resource.id, entry.resource.location)

    # print("Number of encounters found: ", len(encounters))
    # # print(encounters[0]['id'])
    
    # for enc in encounters:
    #     print("Encounter ID: ", enc.id)
    #         # Check if the 'location' field exists in the encounter resource
    #     if 'location' in enc and len(enc['location']) > 0:
    #         location_ref = enc['location'][0]['location']['reference']
    #         location_display = enc['location'][0]['location'].get('display', 'n/a')
    #         print(f"Location Reference: {location_ref}, Location Display: {location_display}")
    #     else:
    #         print("Location details not available.")


if __name__ == '__main__':

    # asyncio.run(main())
    asyncio.run(main_with_include())