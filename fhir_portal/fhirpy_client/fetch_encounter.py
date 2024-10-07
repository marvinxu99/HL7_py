from fhir_portal.fhirpy_client.fhir_client import get_fhir_client  # Import the client configuration module
from fhir_portal.fhirpy_client.fetch_location import fetch_location_by_ref


async def fetch_encounters():
    try: 
        # Create an instance
        client = get_fhir_client()

        # Search for encounters
        resources = client.resources('Encounter')  # Return lazy search set
        # by patient
        resources = resources.search(subject='Patient/example').limit(10)
        # by encounter id
        # resources = resources.search(_id='example2').limit(10)
        encounters = await resources.include('Encounter', 'location').fetch()  # Returns list of AsyncFHIRResource

        return [enc.serialize() for enc in encounters]

    except Exception as e:
        print(f"An error occurred while fetching encounters: {str(e)}")
        return []


async def fetch_encounter_by_id(enc_id):
    try: 
        # Create an instance
        client = get_fhir_client()

        # Search for encounters
        resources = client.resources('Encounter')  # Return lazy search set
        # by encounter id
        # resources = resources.search(_id=id).include('Encounter', 'location')     # TODO: include does not worrk
        resources = resources.search(_id=enc_id)                                   # TODO: include does not worrk
        
        encounter = await resources.get()
        
        print(f"Encounter ID: {encounter['id']}")
            
        # If location information is included, print location details
        if 'location' in encounter and len(encounter['location']) > 0:

            # TODO: FHIR R5 - multiple locations 
            # for loc in encounter['location']:
            #     location_ref = loc['location']['reference']
            #     location_display = loc['location'].get('display', 'n/a')
            #     print(f"Location Reference: {location_ref}, Location Display: {location_display}")

            #     location = await fetch_location_by_ref(location_ref)

            #     if location:
            #         print("Loc Name: ", location['name'])
            #     else:
            #         print("Location details not available.")

            # For now, only get the first location
            loc = encounter['location'][0]
            location_ref = loc['location']['reference']
            location_display = loc['location'].get('display', 'n/a')
            print(f"Location Reference: {location_ref}, Location Display: {location_display}")

            location = await fetch_location_by_ref(location_ref)

            if location:
                print("Loc Name: ", location['name'])
            else:
                print("Location details not available.")

        return encounter.serialize()

    except Exception as e:
        print(f"An error occurred while fetching encounters: {str(e)}")
        return None


if __name__ == '__main__':
    import asyncio
    
    #encounters = asyncio.run(fetch_encounters())
    # for e in encounters:
    #     print(e)
    
    encounter = asyncio.run(fetch_encounter_by_id('example2'))
    print(encounter)
    
