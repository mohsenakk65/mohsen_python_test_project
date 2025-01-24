
import requests

from utils.configs import *
import pytest

class get_tenant_identities:
    def __init__(self, token, tenant_id, national_id, identity_type):
        self.url = DEV_Url_maker("admin-panel/tenant-identities" )
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }
        self.params ={
            "tenant_id": tenant_id,
            "national_id":national_id,
            "identity_type":identity_type
        }




    def get_tenant_identities(self, tenant_id: str, national_id: str, identity_type: str):
        """
        Get tenant identities.

        Args:
            tenant_id (str): Tenant id.
            national_id (str): National id.
            identity_type (str): Identity type.

        Returns:
            requests.Response: Response object.
        """
        url = self.url + f"/{tenant_id}/{national_id}/{identity_type}"
        response = requests.get(url=url, headers=self.headers)
        return response