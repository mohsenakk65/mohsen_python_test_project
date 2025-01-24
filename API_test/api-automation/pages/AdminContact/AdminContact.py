
import requests

from utils.configs import *
import pytest

class AdminFacilitator:
    def __init__(self, token, TenantId, TenantIdentityId):
        self.url = DEV_Url_maker("/admin-panel/contacts")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }
        self.params = {
            "TenantId":TenantId,
            "TenantIdentityId":TenantIdentityId}

    def get_admin_panel_contract_by_tenantId (self):
        response  = requests.get(url = self.url, headers= self.headers, params= self.params)
        return response

    def get_admin_contract_update(self, payload , FacilitatorId ):
        response  = requests.put(url = self.url+ f"/{FacilitatorId}", headers= self.headers, json= payload)
        return response

