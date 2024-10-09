import asyncio
from fhirpy import AsyncFHIRClient


token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWFydmlueHUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ4MTk4YWUwLWY2ZWItNDE3MC1iOTRmLWRmNTFjMzAwNTc2NyIsImp0aSI6ImE0YmRlODY0LTkwYTAtNDdlNi05NzczLTAzNDdjOTRiNjE2NCIsImV4cCI6MTcyODI2OTYyMywiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.wNccto2gIL73B56xEdN2kUCTYy5-NVQo9bnvCVXlFi8"

# Define the FHIR client (ensure the FHIR server URL is correct)
client = AsyncFHIRClient(
    url='https://fhir.simplifier.net/mxfhir',
    authorization=f'Bearer {token}',
    extra_headers={
        'Accept': 'application/fhir+json'
    }
)

# The CareTeam data from your provided JSON
care_team_data = {
    "resourceType": "CareTeam",
    "id": "example",
    "text": {
        "status": "generated",
        "div": '<div xmlns="http://www.w3.org/1999/xhtml">Care Team</div>'
    },
    "contained": [{
        "resourceType": "Practitioner",
        "id": "pr1",
        "name": [{
            "family": "Dietician",
            "given": ["Dorothy"]
        }]
    }],
    "identifier": [{
        "value": "12345"
    }],
    "status": "active",
    "category": [{
        "coding": [{
            "system": "http://loinc.org",
            "code": "LA27976-2",
            "display": "Encounter-focused care team"
        }]
    }],
    "name": "Peter James Charlmers Care Team for Inpatient Encounter",
    "subject": {
        "reference": "Patient/example",
        "display": "Peter James Chalmers"
    },
    "period": {
        "end": "2013-01-01"
    },
    "participant": [{
        "role": {
            "text": "responsiblePerson"
        },
        "member": {
            "reference": "Patient/example",
            "display": "Peter James Chalmers"
        }
    }, {
        "role": {
            "text": "adviser"
        },
        "member": {
            "reference": "#pr1",
            "display": "Dorothy Dietician"
        },
        "onBehalfOf": {
            "reference": "Organization/f001"
        },
        "coverageTiming": {
            "repeat": {
                "boundsPeriod": {
                    "start": "2010-12-23",
                    "end": "2013-01-01"
                },
                "frequency": 1,
                "period": 1,
                "periodUnit": "d",
                "dayOfWeek": ["mon"],
                "when": ["MORN"]
            }
        }
    }],
    "managingOrganization": [{
        "reference": "Organization/f001"
    }]
}

# Async function to create the CareTeam resource
async def create_care_team():
    care_team = client.resource('CareTeam', **care_team_data)
    await care_team.save()
    print(f"CareTeam created with ID: {care_team.id}")


# Run the async function
if __name__ == "__main__":
    asyncio.run(create_care_team())
