from fhirpy import AsyncFHIRClient

def get_fhir_client():
    """
    This function returns an instance of AsyncFHIRClient with the configuration settings.
    """
    client = AsyncFHIRClient(
        'https://fhir.simplifier.net/mxfhir',
        None,
        {
            'Accept': 'application/fhir+json'
        }
    )
    return client