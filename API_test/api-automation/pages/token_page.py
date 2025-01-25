from http.client import responses
from utils.helpers import *
import requests

from utils.configs import *

class   token_page:
    def __init__(self):

        self.token_url = DEV_TOKEN_URL("accounts/login")
        self.HEADERS = {
            "accept": "text/plain",
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkQwMUQ1NkY1OUYxQTgxNzVGNTYxNjIxRDM5RjlCOUE0IiwidHlwIjoiYXQrand0In0.eyJpc3MiOiJodHRwOi8vMzEuMjE0LjE3My4yMDA6ODA4MCIsIm5iZiI6MTczNTE1NDg4OCwiaWF0IjoxNzM1MTU0ODg4LCJleHAiOjE3MzUxNTg0ODgsInNjb3BlIjpbImVtYWlsIiwib3BlbmlkIiwicHJvZmlsZSIsInJvbGVzIl0sImFtciI6WyJwd2QiXSwiY2xpZW50X2lkIjoia2VlcGFfaWRlbnRpdHlfYWRtaW4iLCJzdWIiOiJjZWEwNjkwOC0yMWRlLTQ2Y2EtYWY4OS1mODdmZmFlNjUxMzMiLCJhdXRoX3RpbWUiOjE3MzUxNTQ4ODgsImlkcCI6ImxvY2FsIiwidXNlcl9uYW1lIjoiTWFqaWQiLCJmaXJzdF9uYW1lIjoiXHUwNjQ1XHUwNjJDXHUwNkNDXHUwNjJGIiwibGFzdF9uYW1lIjoiXHUwNjMzXHUwNjQxXHUwNkNDXHUwNjJGXHUwNjI3XHUwNjMxXHUwNkNDIiwidGVuYW50X2lkIjoiMSIsInBlcm1pc3Npb25zIjpbIlVzZXJMaXN0IiwiQ3JlYXRlVXNlciIsIkFkZFVzZXIiLCJFZGl0VXNlciJdLCJqdGkiOiJGNzE5NjVEMDIzNTIxN0MxMkJGQzU3OTkzQUU2ODBCQiJ9.SOGtIMlwG-bee_l-PBYmOTxQ6oq9oFrWoXzpGt-U0wd0Yt_wY4LEP8wstSvQRM3MFNeBhSrjoKvSASuziDYKK0hkGVZHkBK3q8eww8PSRL5de-eyGeYORkESVw265NxanP64fbkTtVZxzKU1h7xroExvu4tleQLre2xrmeLXY6cQqO--ngTjBFGz7y1eFEwM0MgTxfQyX-JeBbQfu71znIdpQZQm-daROn0tovlT1FddDU-ed3pIkuqp1WLZJygDnanVebfZ7lLQezBa4jp_D4KIUDck2pqf7GMxwp4Y4gB9oSLy78KqlWrSF1Mqli4k3FWfIsNg3wjI0zLyeX8V9Q"
        }

    def get_token(self):
        payload = read_json_file("AdminUserLogin", "DataFile")
        response = requests.post(url=self.token_url, headers=self.HEADERS, json=payload)
        print(response)
        validate_response(response, 200)
        assert response.status_code == 200
        return response


