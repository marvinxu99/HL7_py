import asyncio
# from fhir_client_auto_token import get_fhir_client
from fhir_client import get_fhir_client


async def main():
    client = get_fhir_client()


    # Search for a Patient
    patient = await client.resources('Patient').search(_id='f201').get()
    print(patient.serialize())

    print("==== search======")

    # Search for observations by patient ID
    observations = await client.resources('Observation').search(patient=patient['id']).fetch_all()
    for obs in observations:
        print(obs.serialize())

    print("==== reverse search======")
    # Reverse search  --NOT WORKING AS EXPECTED!!!!!!
    # Search for observations with code=8310-5 (which is related to the body temperature). 
    # From every observation found retrieves a reference to the Patient this observation refers to
    observations2 = await client.resources('Patient').has('Observation', 'patient', code='8310-5').fetch()
    for obs in observations2:
        print(obs.serialize())
    

if __name__ == '__main__':
    asyncio.run(main())