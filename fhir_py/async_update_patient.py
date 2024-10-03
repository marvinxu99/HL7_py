import asyncio
from fhirpy import AsyncFHIRClient

async def main():

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWFydmlueHUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ4MTk4YWUwLWY2ZWItNDE3MC1iOTRmLWRmNTFjMzAwNTc2NyIsImp0aSI6IjBmMDMwYzEyLWRlZjUtNDk2My04NWEwLTQ5NmU0ZmYzZmI0ZiIsImV4cCI6MTcyNzk5ODk0OCwiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.6D1ZE9-QXIH6_D2NyAN8wsdYWJIZYKx0cFsr3zPWOuc"

    # Create an instance
    client = AsyncFHIRClient(
        url='https://fhir.simplifier.net/mxfhir',
        authorization=f'Bearer {token}',
        extra_headers={
            'Accept': 'application/fhir+json'
        }
    )

    # Search for patient
    resources = client.resources('Patient')  # Return lazy search set
    patient = await resources.search(gender="male").first()
    # patients = await resources.fetch()  # Returnslist of AsyncFHIRResource
    if patient:
        print(patient['name'])
    else:
        print("No patient found")

    #Update patient resource
    patient.name = [
                    {
                        "use": "official",
                        "family": "Xu1",
                        "given": [
                            "Wesley8",
                            "Alias Name" 
                        ]
                    }
                ]
    try:
        resp = await patient.save()
        print("Update patient successfull:", resp.serialize())

    except Exception as err:
        print("Error in creating patient:", err)
    

    # # Create Patient resource
    # patient= client.resource(
    #             "Patient",
    #             active=False,
    #             name= 
    #             gender="male",
    #             address=[
    #                 {
    #                     "use": "home",
    #                     "text": "test street",
    #                     "city": "Burnaby"
    #                 }
    #             ]
    #     )
    



    # # Create Organization resource
    # organization = client.resource(
    #     'Organization',
    #     name='beda.software',
    #     active=False
    # )
    # await organization.save()

    # # Update (PATCH) organization. Resource support accessing its elements
    # # both as attribute and as a dictionary keys
    # if organization['active'] is False:
    #     organization.active = True
    # await organization.save(fields=['active'])
    # # `await organization.patch(active=True)` would do the same PATCH operation

    # # Get patient resource by reference and delete
    # patient_ref = client.reference('Patient', 'new_patient')
    # # Get resource from this reference
    # # (throw ResourceNotFound if no resource was found)
    # patient_res = await patient_ref.to_resource()
    # await patient_res.delete()

    # # Iterate over search set
    # org_resources = client.resources('Organization')
    # # Lazy loading resources page by page with page count = 100
    # async for org_resource in org_resources.limit(100):
    #     print(org_resource.serialize())


if __name__ == '__main__':
    asyncio.run(main())