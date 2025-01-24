
import requests

from utils.configs import *
import pytest


class AdminUser:
    def __init__(self, token, ):
        self.url = dev_url_maker("client-managements", "admin-panel/users")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "text/plain",

        }


    def get_create_user(self , payload ):
        response = requests.post(self.url, headers=self.headers, json=payload)
        return response

    def get_update_user(self , payload , UserId ):

        response  = requests.put(url = self.url + f"/{UserId}", headers= self.headers, json= payload)
        return response

    def get_user_internal_projectmanagers(self  ):

        response  = requests.get(url = self.url + "/internal-project-managers" , headers= self.headers)
        return response


    def get_user_by_user_entitytypes(self  ):

        response  = requests.get(url = self.url + "/user-entity-types" , headers= self.headers)
        return response

    def get_admin_users(self ):
        response = requests.get(url=self.url, headers=self.headers)

        return response

