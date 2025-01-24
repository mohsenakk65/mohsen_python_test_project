from http.client import responses

import requests

from utils.configs import *
import pytest
class AdminTenant:
    def __init__(self, token, ):
        self.url = DEV_Url_maker("/admin-panel/tenants")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }

    def get_create_tenants(self , payload ):
        response = requests.post(self.url, headers=self.headers, json=payload)
        return response

    def get_update_tenants(self , payload , TenantId ):
        response  = requests.put(url = self.url + f"/{TenantId}", headers= self.headers, json= payload)
        return response

    def get_tenants(self , TenantId ):
        response  = requests.get(url = self.url + f"/{TenantId}", headers= self.headers)
        return response

    def get_tenant(self):

        response = requests.get( url = self.url , headers=self.headers)
        return response



