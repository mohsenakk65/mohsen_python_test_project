
import requests

from utils.configs import *
import pytest

class admin_panel_financiers:
    def __init__(self, token, financierId):
        self.url = DEV_Url_maker("/admin-panel/tenant-identities")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }
        self.params = {
            "PageIndex": 0,
            "PageSize": 10,
            "financierId": financierId

        }



    def get_create_financier_tenant_identities(self, payload, financierId):


        response  = requests.get(url = self.url, headers= self.headers, json= payload)
        return response

    def get_update_financier_tenant_identities(self, payload ):


        response  = requests.put(url = self.url, headers= self.headers, json= payload, params=
        self.params)
        return response

    def get_financier_tenant_identities_by_id(self, financierId ):


        response  = requests.get(url = self.url + f"/{financierId}", headers= self.headers)
        return response

    def get_financier_tenant_identities_filter(self, TenantId, LegalTypeId, PersonType, PageIndex, PageSize ):

        response  = requests.get(url = self.url + f"/{TenantId}/{LegalTypeId}/{PersonType}/{PageIndex}/{PageSize}", headers= self.headers)
        return response



