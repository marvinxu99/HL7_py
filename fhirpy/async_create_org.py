import asyncio
from fhirpy import AsyncFHIRClient


async def main():

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWFydmlueHUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ4MTk4YWUwLWY2ZWItNDE3MC1iOTRmLWRmNTFjMzAwNTc2NyIsImp0aSI6ImM5MWNlM2JiLWZhODYtNGQ5YS04MDU5LTllYzkxZWExZDc4YSIsImV4cCI6MTcyNzk2MTg0MSwiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.5NsB10qq3cCdqolX75F506UmN0CXTwFZUVum8hkSslM"

    # Create an instance
    client = AsyncFHIRClient(
        url='https://fhir.simplifier.net/mxfhir',
        authorization=f'Bearer {token}',
        extra_headers={
            'Accept': 'application/fhir+json'
        }
    )

    # # Create Organization resource
    organization = client.resource(
        'Organization',
        name='beda.software',
        active=False
    )
    resp = await organization.save()
    print(resp.serialize())


if __name__ == '__main__':
    asyncio.run(main())