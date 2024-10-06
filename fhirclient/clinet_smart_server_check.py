from fhirclient import client

def smart_server_check():
    settings = {
        'app_id': 'my_web_app',
        'api_base': 'https://r4.smarthealthit.org'
    }
    smart = client.FHIRClient(settings=settings)

    print(smart.ready)
    # prints `False`

    smart.prepare()
    # prints `True` after fetching CapabilityStatement
    
    print(smart.ready)
    # prints `True`
    
    smart.prepare()
    # prints `True` immediately
    
    print(smart.authorize_url)
    # is `None`

if __name__ == "__main__":
    smart_server_check()