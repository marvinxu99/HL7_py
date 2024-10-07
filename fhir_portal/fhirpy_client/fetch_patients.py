from fhir_client import get_fhir_client  # Import the client configuration module


async def fetch_patients():
    try: 
        # Create an instance
        client = get_fhir_client()

        # Search for patients
        resources = client.resources('Patient')  # Return lazy search set
        resources = resources.search(name='Marvin').limit(10).sort('name')
        patients = await resources.fetch()  # Returns list of AsyncFHIRResource

        return [pt.serialize() for pt in patients]

    except Exception as e:
        print(f"An error occurred while fetching patients: {str(e)}")
        return []


if __name__ == '__main__':
    import asyncio
    patients = asyncio.run(fetch_patients())
    for pt in patients:
        print(pt)
