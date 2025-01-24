
import requests

from utils.configs import *
import pytest

class AdminFacilitator:
    def __init__(self, token,TenantId, LegalTypeId, PersonType ):
        self.url = DEV_Url_maker("/admin-panel/facilitators")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }
        self.params = {
            "TenantId" : TenantId,
            "LegalTypeId":LegalTypeId,
            "PersonType": PersonType




        }


    def get_Create_Facilitator(self, payload):
        response = requests.post(self.url, headers=self.headers, json=payload)
        return response

    def get_update_Facilitator(self , payload , FacilitatorId ):

        response  = requests.put(url = self.url + f"/{FacilitatorId}", headers= self.headers, json= payload)
        return response

    def get_Facilitator_by_id(self , FacilitatorId ):

        response  = requests.get(url = self.url + f"/{FacilitatorId}", headers= self.headers)
        return response



    def get_facilitator_filter(self ):
        response = requests.get(url= self.url,headers=self.headers,  params=self.params)
        return response


