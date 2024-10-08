import asyncio
from fhirpy import AsyncFHIRClient


token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWFydmlueHUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ4MTk4YWUwLWY2ZWItNDE3MC1iOTRmLWRmNTFjMzAwNTc2NyIsImp0aSI6ImZmZTc4NDBiLTAyYzItNGIyYS1hNDk3LWQwNmIwMDE0YWRmNiIsImV4cCI6MTcyODQ1NzY0MiwiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.Ddd3J1tq3XPwNJQnDJVGqSGpq4_HR_bHfDamnO2SebU"

# Define the FHIR client (ensure the FHIR server URL is correct)
client = AsyncFHIRClient(
    url='https://fhir.simplifier.net/mxfhir',
    authorization=f'Bearer {token}',
    extra_headers={
        'Accept': 'application/fhir+json'
    }
)

# The CareTeam data from your provided JSON
loc_data = {
  "resourceType" : "Location",
  "id" : "amb001",
  "text" : {
    "status" : "generated",
    "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">Mobile Clinic</div>"
  },
  "status" : "active",
  "name" : "BUMC Ambulance",
  "description" : "Ambulance provided by Burgers University Medical Center",
  "mode" : "kind",
  "type" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
      "code" : "AMB",
      "display" : "Ambulance"
    }]
  }],
  "contact" : [{
    "telecom" : [{
      "system" : "phone",
      "value" : "2329",
      "use" : "mobile"
    }]
  }],
  "form" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/location-physical-type",
      "code" : "ve",
      "display" : "Vehicle"
    }]
  },
  "managingOrganization" : {
    "reference" : "Organization/f001"
  }
}


# Async function to create the CareTeam resource
async def create_location():
    loc = client.resource('Location', **loc_data)
    await loc.save()
    print(f"Location created with ID: {loc.id}")


# Run the async function
if __name__ == "__main__":
    asyncio.run(create_location())
