from http.client import responses

import requests

from utils.configs import *
import pytest


class Facilitator:
    def __init__(self, token):
        self.fas_url = dev_url_maker("client-managements", "admin-panel/facilitators")

        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }


    def create_facilitator(self, payload):
        response = requests.post(self.fas_url, headers=self.headers, json=payload)
        return response

    def get_fasilitators_filter(self, params ):
        response = requests.get(self.fas_url, headers=self.headers , params= params)
        return response


    def get_fasilitator_byId(self, Id ):

        response = requests.get(url=self.fas_url + f"1{Id}", headers=self.headers )
        return response


    def update_fasilitator_byId(self, Id ):

        response = requests.put(url=self.fas_url + f"/{Id}", headers=self.headers )

        return response

