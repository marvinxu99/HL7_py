# -*- coding: utf-8 -*-

# Zato
from zato.server.service import Service

class FHIService1(Service):
    name = 'demo.fhir.1'

    def handle(self) -> 'None':

        # Connection to use
        conn_name = 'mxfhir.read'

        with self.out.hl7.fhir[conn_name].conn.client() as client:

            # This is how we can refer to patients
            patients = client.resources('Patient')

            # Get all active patients, sorted by their birth date
            result = patients.sort('active', '-birthdate')

            # Log the result that we received
            for elem in result:
                self.logger.info('Received -> %s', elem['name'])