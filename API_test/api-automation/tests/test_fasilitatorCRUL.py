import pytest
import json
from pages.Facilitator import *
from pages.tenant_page import tenantservises
from pages.token_page import *
from utils.random_values import *
from utils.helpers import validate_response, validate_schema

class Test_Facilitator:
    """
    test admin customer crud operations
    """
    @pytest.fixture(scope="module")
    def access_token(self):
        accessToken = token_page().get_token()
        print(accessToken)
        token = accessToken.json()["accessToken"]
        return token

    @pytest.fixture(scope="module")
    def tenant_id (self, access_token):
        tenant_service = tenantservises(access_token)
        tenant_data = tenant_payload()
        response = tenant_service.create_tenant(tenant_data).json()
        return response

    def test_facilitator_create(self, access_token, tenant_id):
        facilitator_service = Facilitator(access_token)
        facilitatorData = read_json_file("facilitators","DataFile/")
        modifiedPayload = modify_json_data(facilitatorData, {"tenantId":tenant_id, "name": "keepaFas"})

        response = facilitator_service.create_facilitator(modifiedPayload)
        print(response.status_code)
        print(tenant_id)
        print(response.json())
        validate_response(response, 201)
