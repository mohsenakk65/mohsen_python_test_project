from http.client import responses

import requests

from utils.configs import *
import pytest


from utils.configs import *

class  financeiservises:
    def __init__(self, token):
        self.url = dev_url_maker("client-managements", "admin-panel/financiers")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }



    def Create_financier(self, payload):

        response  = requests.post(url = self.url,json= payload, headers= self.headers)
        return response



    def inquiry_financier_filter(self, tenant_id , legal_type_id , person_type , page_index , page_size ):

        params = {"tenantId": tenant_id, "legalTypeId": legal_type_id, "personType": person_type, "pageIndex": page_index, "pageSize": page_size}
        response  = requests.get(url = self.url , params= params, headers= self.headers)
        return response

    def  inquiry_financier_by_id(self, financier_id ):
        response = requests.get(url = self.url + f"/{financier_id}", headers= self.headers)
        return response

    def update_financier_by_id(self, payload, financier_id ):

        response  = requests.put(url = self.url + f"/{financier_id}", headers= self.headers, json= payload)
        return response




