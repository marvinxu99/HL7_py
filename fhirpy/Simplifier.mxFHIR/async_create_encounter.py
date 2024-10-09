import asyncio
from fhirpy import AsyncFHIRClient


async def main():

    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWFydmlueHUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ4MTk4YWUwLWY2ZWItNDE3MC1iOTRmLWRmNTFjMzAwNTc2NyIsImp0aSI6IjA4MGIxYjc2LWM3MDgtNGYzZC1iM2FiLTc0YjZhN2UyMDVhMyIsImV4cCI6MTcyODM0ODY1NSwiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.ALdRabwG9LNty42dgemrF9fHvIfbstVkckto-6zDmGk"

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
        id="example3",
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