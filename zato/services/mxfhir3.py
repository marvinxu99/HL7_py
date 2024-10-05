# -*- coding: utf-8 -*-

# Zato
from zato.server.service import Service

# ##############################################################################

class MyService(Service):
    """ Returns user details by the person's name.
    """
    name = 'mxfhir3.get.patients'

       
    # Connection to use
    conn_name = 'mxfhir.read'

    def handle(self):

        # Connection to use
        conn_name = 'mxfhir.read'

        with self.out.hl7.fhir[conn_name].conn.client() as client:

            # This is how we can refer to patients
            patients = client.resources('Patient')

            # Get all active patients, sorted by their birth date
            result = patients.sort('active', '-birthdate').fetch()

            # Log the result that we received
            for elem in result:
                self.logger.info('Received -> %s', elem['name'])
                
            #Now, produce the response for our caller
            # self.response.payload = {
            #   'user_type': "test_type",
            #   'account_no': "123456",
            #   'account_balance': "345.67",
            # }
            self.response.payload = {
                'patients': [patient.serialize() for patient in result] 
            }

# ##############################################################################