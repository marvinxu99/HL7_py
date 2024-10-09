import asyncio
# from fhir_client_auto_token import get_fhir_client
from fhir_client import get_fhir_client


async def main():
    client = get_fhir_client()

    data = {
        "id": "practitioner_kelly_smith",
        "name": [
          {
            "given": [
              "Kelly"
            ],
            "family": "Smith",
            "text": "Kelly Smith"
          }
        ],
        "qualification": [
          {
            "code": {
              "coding": [
                {
                  "system": "http://hl7.org/fhir/v2/0360/2.7",
                  "code": "PHD"
                }
              ]
            }
          }
        ],
        "resourceType": "Practitioner",
        "meta": {
          "lastUpdated": "2018-11-02T05:54:11.308Z",
          "versionId": "65",
          "tag": [
            {
              "system": "https://aidbox.app",
              "code": "created"
            }
          ]
        }
      }
    
    await client.resource('Practitioner', **data).save()

    data = {
        "id": "practitioner_adam_ainsley",
        "name": [
          {
            "given": [
              "Adam"
            ],
            "family": "Ainsley",
            "text": "Adam Ainsley"
          }
        ],
        "qualification": [
          {
            "code": {
              "coding": [
                {
                  "system": "http://hl7.org/fhir/v2/0360/2.7",
                  "code": "PHD"
                }
              ]
            }
          }
        ],
        "resourceType": "Practitioner",
        "meta": {
          "lastUpdated": "2018-11-02T05:54:11.363Z",
          "versionId": "66",
          "tag": [
            {
              "system": "https://aidbox.app",
              "code": "created"
            }
          ]
        }
      }
    await client.resource('Practitioner', **data).save()


if __name__ == '__main__':
    asyncio.run(main())