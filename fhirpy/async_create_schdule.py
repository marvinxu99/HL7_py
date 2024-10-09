import asyncio
# from fhir_client_auto_token import get_fhir_client
from fhir_client import get_fhir_client


async def main():
    client = get_fhir_client()

    data = {
      "resourceType" : "Schedule",
      "id" : "example",
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n      Burgers UMC, South Wing, second floor Physiotherapy Schedule\n\t\t</div>"
      },
      "identifier" : [{
        "use" : "usual",
        "system" : "http://example.org/scheduleid",
        "value" : "45"
      }],
      "active" : True,
      "serviceCategory" : [{
        "coding" : [{
          "system" : "http://terminology.hl7.org/CodeSystem/service-category",
          "code" : "17",
          "display" : "General Practice"
        }]
      }],
      "serviceType" : [{
        "concept" : {
          "coding" : [{
            "system" : "http://terminology.hl7.org/CodeSystem/service-type",
            "code" : "57",
            "display" : "Immunization"
          }]
        }
      }],
      "specialty" : [{
        "coding" : [{
          "system" : "http://snomed.info/sct",
          "code" : "408480009",
          "display" : "Clinical immunology"
        }]
      }],
      "name" : "Burgers UMC, South Wing - Immunizations",
      "actor" : [{
        "reference" : "Location/amb001",
        "display" : "Burgers UMC, South Wing, second floor"
      }],
      "planningHorizon" : {
        "start" : "2013-12-25T09:15:00Z",
        "end" : "2013-12-25T09:30:00Z"
      },
      "comment" : "The slots attached to this schedule should be specialized to cover immunizations within the clinic"
    }
    
    await client.resource('Schedule', **data).save()



if __name__ == '__main__':
    asyncio.run(main())