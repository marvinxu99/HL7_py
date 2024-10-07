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
    encounter = client.resource(
        "Encounter",
        id="example2",
        text={
            "status": "generated",
            "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Encounter with patient @example</div>"
        },
        status="in-progress",
        subject={
            "reference": "Patient/example"
        }        
    )

    encounter['class']=[{
        "coding" : [{
        "system" : "http://terminology.hl7.org/CodeSystem/v3-ActCode",
        "code" : "IMP",
        "display" : "inpatient encounter"
        }]
    }],

    try:
        resp = await encounter.save()
        print("Creating Encounter successfull:", resp.serialize())

    except Exception as err:
        print("Error in creating Encounter:", err)


if __name__ == '__main__':
    asyncio.run(main())