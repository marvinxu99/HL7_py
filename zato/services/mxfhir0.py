# -*- coding: utf-8 -*-

# Zato
from zato.server.service import Service

class MyService(Service):
    name = 'mxfhir0.general.info'

    def handle(self):
        self.response.payload = {
                'response': "Pease use a specific API endpointa" 
        }
