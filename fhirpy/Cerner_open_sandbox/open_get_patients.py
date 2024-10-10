import asyncio
from fhir_client import get_fhir_client


async def main():
    client = get_fhir_client()


    # Getting multiple patients

    # patients = await client.resources('Patient').search(_id='12742400').fetch()  # Returns list of AsyncFHIRResource
    # patients = await client.resources('Patient').search(family='PETERS').fetch()  # Returns list of AsyncFHIRResource
    # for pt in patients:
    #     # print(pt.serialize())
    #     print(
    #         "ID: ", pt['id'],
    #         "\n Name:", pt['name'][0]['given'][0], pt.get_by_path('name.0.family') 
    #     )

    print("=======================")

    # Search for a Patient
    # patients = await client.resources('Patient').search(_id='12742400').fetch()  # Returns list of AsyncFHIRResource
    patients = await client.resources('Patient').search(_id='12744734').fetch()
    print(patients[0].serialize())

    print("=======================")
    practitioners = await client.resources('Practitioner').search(_id='12744688').fetch()
    print(practitioners[0].serialize())
    

    


    

if __name__ == '__main__':
    asyncio.run(main())