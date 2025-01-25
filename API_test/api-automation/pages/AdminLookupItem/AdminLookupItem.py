from http.client import responses

import requests

from utils.configs import *
import pytest


class AdminLookup:
    def __init__(self, token, ):
        self.url1 = dev_url_maker("client-managements", "admin-panel/lookup-items")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }

    def get_lookupItems(self, Type):
        url2 = f"{self.url1}/{Type}"
        response = requests.get(url2, headers=self.headers)

        return response
