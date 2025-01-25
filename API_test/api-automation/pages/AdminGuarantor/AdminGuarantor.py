
import requests

from utils.configs import *
import pytest


class Admin_Guarantor:
    def __init__(self, token,TenantId,LegalTypeId ,  PersonType):
        self.url = DEV_Url_maker("/admin-panel/guarantors")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }
        self.params = {

            "TenantId" :TenantId,
            "LegalTypeId":LegalTypeId,
            "PersonType":PersonType
        }

    def get_Create_Guarantor(self, payload):
        response  = requests.post(url = self.url,json= payload, headers= self.headers)
        return  response


    def get_update_Guarantor(self , payload , GuarantorId ):

        response  = requests.put(url = self.url + f"/{GuarantorId}", headers= self.headers, json= payload)
        return response

    def get_Guarantor_by_id(self , GuarantorId ):

        response  = requests.get(url = self.url + f"/{GuarantorId}", headers= self.headers)
        return response

    def get_Guarantor_filter(self ):

        response  = requests.get(url = self.url , headers= self.headers, params=self.params)
        return response



