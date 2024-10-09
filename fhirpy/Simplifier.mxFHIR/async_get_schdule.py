import asyncio
# from fhir_client_auto_token import get_fhir_client
# from fhir_client import get_fhir_client
from fhirpy import AsyncFHIRClient


async def main():
    # client = get_fhir_client()

    # Create an instance
    client = AsyncFHIRClient(
        'https://fhir.simplifier.net/mxfhir',
        None,
        {
            'Accept': 'application/fhir+json'
        }
        # authorization='Bearer TOKEN',
    )

    #result = await client.resources('Schedule').search(_id='example').include('Schedule', 'actor').fetch()
    resources = client.resources('Schedule')
    result = await resources.fetch_all()

    print(result)



if __name__ == '__main__':
    asyncio.run(main())