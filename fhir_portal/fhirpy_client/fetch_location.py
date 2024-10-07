from fhir_portal.fhirpy_client.fhir_client import get_fhir_client  # Import the client configuration module


async def fetch_location_by_ref(loc_ref):
    # Create an instance of the FHIR client
    client = get_fhir_client()

    try: 
        # Fetch the location resource using the reference
        # example loc ref: https://fhir.simplifier.net/mxfhir/Location/amb
        location = await client.resources('Location').search(_id=loc_ref.split('/')[-1]).get()

        return location.serialize()

    except Exception as e:
        print(f"An error occurred while fetching patients: {str(e)}")
        return None
       

if __name__ == '__main__':
    import asyncio

    location = asyncio.run(fetch_location_by_ref('https://fhir.simplifier.net/mxfhir/Location/amb'))
    print(location)
