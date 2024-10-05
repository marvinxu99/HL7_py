# -*- coding: utf-8 -*-

# Zato
from zato.server.service import Service

class CreatePatient(Service):
    name = 'mxfhir2.create'

    def handle(self) -> 'None':

        # Connection to use
        conn_name = 'mxfhir.create'
        
        patient_data = {
                  "resourceType": "Patient",
                  "name": [
                    {
                      "family": "Smith",
                      "given": [
                        "John"
                      ]
                    }
                  ],
                  "gender": "male",
                  "birthDate": "1982-05-23"
            }
                
        with self.out.hl7.fhir[conn_name].conn.client() as client:
           
            # First, create a new patient
            #patient = client.resource('Patient')
            response = client.resource("Patient").create(patient_data)

            # Save the patient in the FHIR server
            # patient.save()
            
            # Check the response status and handle it
            if response.status_code == 201:
                patient_id = response.json()["id"]
                self.logger.info(f'Patient created successfully. Patient ID: {patient_id}')
                self.response.payload = {'patient_id': patient_id}
            else:
                self.logger.error(f'Error creating patient: {response.text}')
                self.response.payload = {'error': response.text}
