import requests
from fhirpy import AsyncFHIRClient


token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWFydmlueHUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ4MTk4YWUwLWY2ZWItNDE3MC1iOTRmLWRmNTFjMzAwNTc2NyIsImp0aSI6ImZmZTc4NDBiLTAyYzItNGIyYS1hNDk3LWQwNmIwMDE0YWRmNiIsImV4cCI6MTcyODQ1NzY0MiwiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.Ddd3J1tq3XPwNJQnDJVGqSGpq4_HR_bHfDamnO2SebU"


def get_fhir_client():
    """
    This function returns an instance of AsyncFHIRClient with the configuration settings.
    """
    # Define the FHIR client (ensure the FHIR server URL is correct)
    client = AsyncFHIRClient(
        url='https://fhir.simplifier.net/mxfhir',
        authorization=f'Bearer {token}',
        extra_headers={
            'Accept': 'application/fhir+json'
        }
    )
   
    return client



