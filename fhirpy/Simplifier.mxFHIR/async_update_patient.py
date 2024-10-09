import asyncio
from fhirpy import AsyncFHIRClient

async def main():

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWFydmlueHUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ4MTk4YWUwLWY2ZWItNDE3MC1iOTRmLWRmNTFjMzAwNTc2NyIsImp0aSI6IjBmMDMwYzEyLWRlZjUtNDk2My04NWEwLTQ5NmU0ZmYzZmI0ZiIsImV4cCI6MTcyNzk5ODk0OCwiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.6D1ZE9-QXIH6_D2NyAN8wsdYWJIZYKx0cFsr3zPWOuc"

    # Create an instance
    client = AsyncFHIRClient(
        url='https://fhir.simplifier.net/mxfhir',
        authorization=f'Bearer {token}',
        extra_headers={
            'Accept': 'application/fhir+json'
        }
    )

    # Search for patient
    resources = client.resources('Patient')  # Return lazy search set
    patient = await resources.search(gender="male").first()
    # patients = await resources.fetch()  # Returnslist of AsyncFHIRResource
    if patient:
        print(patient['name'])
    else:
        print("No patient found")

    #Update patient resource
    patient.name = [
                    {
                        "use": "official",
                        "family": "Xu1",
                        "given": [
                            "Wesley8",
                            "Alias Name" 
                        ]
                    }
                ]
    try:
        resp = await patient.save()
        print("Update patient successfull:", resp.serialize())

    except Exception as err:
        print("Error in creating patient:", err)
    

if __name__ == '__main__':
    asyncio.run(main())