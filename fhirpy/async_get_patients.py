import asyncio
from fhirpy import AsyncFHIRClient


async def main():
    # Create an instance
    client = AsyncFHIRClient(
        'https://fhir.simplifier.net/mxfhir',
        None,
        {
            'Accept': 'application/fhir+json'
        }
        # authorization='Bearer TOKEN',
    )

    # Search for patients
    resources = client.resources('Patient')  # Return lazy search set
    
    #resources = resources.search(_name='Marvin').limit(10).sort('name')
    resources = resources.search(_id='f201')

    patients = await resources.fetch()  # Returns list of AsyncFHIRResource

    for pt in patients:
        print(pt.serialize())

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
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    asyncio.run(main())