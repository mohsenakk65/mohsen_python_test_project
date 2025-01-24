
import requests

from utils.configs import *
import pytest

class  tenantservises:
    def __init__(self, token):
        # self.tenantUrl = dev_url_maker("/admin-panel/tenants")
        self.tenantUrl = dev_url_maker("client-managements", "admin-panel/tenants")
        """
        Initialize the tenant service with an authorization token.
        """
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",
        }

    def create_tenant(self, payload):
        """Create a tenant."""
        response = requests.post(url=self.tenantUrl, json=payload, headers=self.headers)
        return response


    def get_tenants(self) -> requests.Response:
        """Get all tenants."""
        response = requests.get(url=self.tenantUrl, headers=self.headers)
        return response

    def     update_tenant(self, payload, tenantId):

        response= requests.put(url=self.tenantUrl + f"/{tenantId}", json=payload, headers= self.headers)
        return response

    def    get_tenants_by_id(self, tenant_id):
        response =requests.get(url= self.tenantUrl + f"/{tenant_id}", headers=self.headers )
        # Debug: Print the response status code and body
        print("Response Status Code:", response.status_code)
        print("Response Body:", response.text)
        return response


