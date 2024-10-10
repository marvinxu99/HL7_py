import asyncio
from fhir_client import get_fhir_client


async def main():
    client = get_fhir_client()
  
    data = {
        "resourceType":"Practitioner",
        "active": True,
        "name":[
            {
                "family":"Williams",
                "given":[
                    "Rory",
                    "James"
                ],
                "prefix":[
                    "Dr."
                ],
                "suffix":[
                    "M.D."
                ],
                "period":{
                    "start":"2019-12-01T00:00:00.000Z"
                }
            }
        ],
        "identifier":[
            {
                "type":{
                    "coding":[
                        {
                            "code":"DEA",
                            "system":"http://terminology.hl7.org/CodeSystem/v2-0203"
                        }
                    ]
                },
                "system":"urn:oid:2.16.840.1.113883.4.814",
                "value":"CW1234563",
                "period":{
                    "start":"2019-12-01T00:00:00.000Z",
                    "end":"2029-12-01T23:59:59.000Z"
                }
            }
        ]
    }
  
    response = await client.resource('Practitioner', **data).save()
    print(response)


if __name__ == '__main__':
    asyncio.run(main())