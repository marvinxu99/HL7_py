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


    # Create Capability resource
    capability = client.resource(
                "CapabilityStatement",
                id="example",
                fhirVersion="5.0.0",
                format=["xml", "json"],
                url="urn:uuid:68d043b5-9ecf-4559-a57a-396e0d452311",
                name="ACMEEHR",
                title="ACME EHR capability statement",
                status="draft",
                experimental=True,
                date="2012-01-04",
                publisher="ACME Corporation",

                implementationGuide=["http://example.org/fhir/us/lab"],
                rest=[{
                    "mode" : "server",
                    "documentation" : "Main FHIR endpoint for acem health",
                    "security" : {
                    "cors" : True,
                    "service" : [{
                        "coding" : [{
                        "system" : "http://hl7.org/fhir/restful-security-service",
                        "code" : "SMART-on-FHIR"
                        }]
                    }],
                    "description" : "See Smart on FHIR documentation"
                    },
                    "resource" : [{
                    "type" : "Patient",
                    "profile" : "http://registry.fhir.org/r5/StructureDefinition/7896271d-57f6-4231-89dc-dcc91eab2416",
                    "supportedProfile" : ["http://registry.fhir.org/r5/StructureDefinition/00ab9e7a-06c7-4f77-9234-4154ca1e3347"],
                    "documentation" : "This server does not let the clients create identities.",
                    "interaction" : [{
                        "code" : "read"
                    },
                    {
                        "code" : "vread",
                        "documentation" : "Only supported for patient records since 12-Dec 2012"
                    },
                    {
                        "code" : "update"
                    },
                    {
                        "code" : "history-instance"
                    },
                    {
                        "code" : "create"
                    },
                    {
                        "code" : "history-type"
                    }],
                    "versioning" : "versioned-update",
                    "readHistory" : True,
                    "updateCreate" : False,
                    "conditionalCreate" : True,
                    "conditionalRead" : "full-support",
                    "conditionalUpdate" : False,
                    "conditionalPatch" : False,
                    "conditionalDelete" : "not-supported",
                    "searchInclude" : ["Patient:organization"],
                    "searchRevInclude" : ["Person:patient"],
                    "searchParam" : [{
                        "name" : "identifier",
                        "definition" : "http://hl7.org/fhir/SearchParameter/Patient-identifier",
                        "type" : "token",
                        "documentation" : "Only supports search by institution MRN"
                    },
                    {
                        "name" : "general-practitioner",
                        "definition" : "http://hl7.org/fhir/SearchParameter/Patient-general-practitioner",
                        "type" : "reference"
                    }]
                    }],
                    "interaction" : [{
                    "code" : "transaction"
                    },
                    {
                    "code" : "history-system"
                    }],
                    "compartment" : ["http://hl7.org/fhir/CompartmentDefinition/patient"]
                }]

            )
    
    try:
        resp = await capability.save()
        print("Creating CapabilityStatement successfull:", resp.serialize())

    except Exception as err:
        print("Error in creating CapabilityStatement:", err)


if __name__ == '__main__':
    asyncio.run(main())