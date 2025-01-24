import requests

from utils.configs import *
import pytest


class adminPanel_orgnization:
    def __init__(self, token):
        self.url = dev_url_maker("client-managements", "admin-panel/organizations")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }

    def create_adminPanel_orgnization(self, payload):
        response = requests.post(url=self.url, headers=self.headers, json=payload)
        return response

    def get_adminPanel_orgnization_by_id(self, tenant_id):
        response = requests.get(url=self.url, headers=self.headers, params=tenant_id)
        return response

    def update_adminPanel_orgnization(self, tenant_id, payload):
        response = requests.put(url=self.url, headers=self.headers, params=tenant_id, json=payload)
        return response

    def get_adminPanel_orgnization_by_id(self, orgnization_id):
        response = requests.get(url=self.url , headers=self.headers , params=orgnization_id)
        return response
