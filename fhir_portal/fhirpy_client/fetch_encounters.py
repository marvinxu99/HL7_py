from fhir_client import get_fhir_client  # Import the client configuration module


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
        encounters = await resources.fetch()  # Returns list of AsyncFHIRResource

        return [enc.serialize() for enc in encounters]

    except Exception as e:
        print(f"An error occurred while fetching encounters: {str(e)}")
        return []


if __name__ == '__main__':
    import asyncio
    encounters = asyncio.run(fetch_encounters())
    for e in encounters:
        print(e)
