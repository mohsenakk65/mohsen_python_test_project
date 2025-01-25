import requests

from utils.configs import *
import pytest


class admin_Customer:
    def __init__(self, token):
        self.url = dev_url_maker("client-managements", "admin-panel/customers")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }


    def get_create_customer(self, payload):
        response = requests.post(url=self.url, headers=self.headers, json=payload)
        return response

    def get_update_customer(self, payload, CustomerId):
        response = requests.put(url=self.url + f"/{CustomerId}", headers=self.headers, json=payload)
        return response

    def get_customer_by_id(self, CustomerId):
        response = requests.get(url=self.url + f"/{CustomerId}", headers=self.headers)
        return response

    def get_customer_filter(self):
        response = requests.get(url=self.url, headers=self.headers, params=self.params)
        return response
