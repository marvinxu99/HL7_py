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

    # Search for patients
    resource = client.resources('Encounter')
    encounter = await resource.search(_id="example1").get()          # Returns one AsyncFHIRResource   
    
    # print(encounter.serialize(), "\n")

    # Add more information
    # encounter['subjectStatus'] = {
    #     "coding" : [{
    #     "system" : "http://terminology.hl7.org/CodeSystem/encounter-subject-status",
    #     "code" : "receiving-care"
    #     }]
    # }

    # Add location information
    encounter['location'] = [{
            "location": {
                "reference": "Location/amb"
            },
            "status": "Completed",
            "period" : {
                "start" : "2015-01-17T16:00:00+10:00",
                "end" : "2015-01-17T16:30:00+10:00"
            }
        }]

    # Update resource
    try:
        resp = await encounter.save()
        print("Encounter updated successfully:", resp.serialize())
    except Exception as err:
        print("Error in updating Encounter:", err)


if __name__ == '__main__':
    asyncio.run(main())