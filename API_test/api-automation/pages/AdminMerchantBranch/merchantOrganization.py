
import requests

from utils.configs import *
import pytest


class merchantOrganization:
    def __init__(self, token, MerchantId):
        self.url = DEV_Url_maker("/admin-panel/merchant-branchs")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }
        self.params = {
            "MerchantId":MerchantId,
            "PageIndex":0,
            "PageSize": 2

        }


    def Create_merchantOrganization(self, payload):

        response  = requests.post(url = self.url,json= payload, headers= self.headers)
        return response

    def get_merchantOrganization_filter(self ):

        response  = requests.get(url = self.url , headers= self.headers , params=self.params)
        return response

    def get_update_merchantOrganization(self , payload , MerchantId ):

        response  = requests.put(url = self.url + f"/{MerchantId}", headers= self.headers, json= payload)
        return response

    def get_merchantOrganization_by_id(self , MerchantId ):

        response  = requests.get(url = self.url + f"/{MerchantId}", headers= self.headers)
        return response



