import requests

from    utils.configs import *


class   lookup_items:

    def     __init__(self, token):

        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }
        self.URL = dev_url_maker("client-managements", "admin-panel/lookup-items")

    def get_lookup_items(self, lookup_type: int) -> requests.Response:
        """Get lookup items for a given type."""
        url = f"{self.URL}/{lookup_type}"
        response = requests.get(url, headers=self.headers)
        return response