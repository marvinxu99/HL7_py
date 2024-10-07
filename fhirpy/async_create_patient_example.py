import asyncio
from fhirpy import AsyncFHIRClient


async def main():

    token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWFydmlueHUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ4MTk4YWUwLWY2ZWItNDE3MC1iOTRmLWRmNTFjMzAwNTc2NyIsImp0aSI6ImE0YmRlODY0LTkwYTAtNDdlNi05NzczLTAzNDdjOTRiNjE2NCIsImV4cCI6MTcyODI2OTYyMywiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.wNccto2gIL73B56xEdN2kUCTYy5-NVQo9bnvCVXlFi8"
    
    # Create an instance
    client = AsyncFHIRClient(
        url='https://fhir.simplifier.net/mxfhir',
        authorization=f'Bearer {token}',
        extra_headers={
            'Accept': 'application/fhir+json'
        }
    )

    # Create Patient resource
    patient= client.resource(
                "Patient",
                id="example",
                active=False,
                name= [
                    {
                        "use": "official",
                        "family": "Xu",
                        "given": [
                            "Wesley9"
                        ]
                    }
                ],
                gender="male",
                address=[
                    {
                        "use": "home",
                        "text": "test street",
                        "city": "Burnaby"
                    }
                ]
        )
    
    try:
        resp = await patient.save()
        print("Creating patient successfull:", resp.serialize())

    except Exception as err:
        print("Error in creating patient:", err)


if __name__ == '__main__':
    asyncio.run(main())