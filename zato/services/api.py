# -*- coding: utf-8 -*-

# Zato
from zato.server.service import Service

# ##############################################################################

class MyService(Service):
    """ Returns user details by the person's name.
    """
    name = 'api.my-service'

    # I/O definition
    input = '-name'
    output = 'user_type', 'account_no', 'account_balance'

    def handle(self):

        # For later use
        name = self.request.input.name or 'partner'

        # REST connections
        crm_conn = self.out.rest['CRM'].conn
        billing_conn = self.out.rest['Billing'].conn

        # Prepare requests
        crm_request = {'UserName':name}
        billing_params = {'USER':name}

        # Get data from CRM
        crm_data = crm_conn.get(self.cid, crm_request).data

        # Get data from Billing
        billing_data = billing_conn.post(self.cid, params=billing_params).data

        # Extract the business information from both systems
        user_type = crm_data['UserType']
        account_no = crm_data['AccountNumber']
        account_balance = billing_data['ACC_BALANCE']

        self.logger.info(f'cid:{self.cid} Returning user details for {name}')

        # Now, produce the response for our caller
        self.response.payload = {
          'user_type': user_type,
          'account_no': account_no,
          'account_balance': account_balance,
        }

# ##############################################################################