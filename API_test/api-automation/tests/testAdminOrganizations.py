import allure
import pytest
import json

from pages.AdminOrgnization import adminpanelOrganizations
from pages.tenant_page import *
from pages.AdminOrgnization.adminpanelOrganizations import *
from pages.token_page import *
from utils.random_values import *
from utils.helpers import validate_response, validate_schema
from allure import *



@allure.suite("AdminOrganizations")

class TestAdminOrganizations:

    @pytest.fixture(scope="class")
    def access_token(self):
        accessToken = token_page().get_token()
        print(accessToken)
        token = accessToken.json()["accessToken"]
        return token

    @pytest.fixture(scope="function")
    def tenant_id(self, access_token):
        tenant = tenantservises(access_token).get_tenants()
        validate_response(tenant, 201)
        return tenant.json()

    TEST_CASES = [
        (0, 9, 400, "شناسه والد سازمان معتبر نمی باشد."),  # Valid type, expected status code 200
        (2, 9, 400, "والد انتخاب شده به مالک زیر ساخت تعلق ندارد."),
        (None, 9, 201, None)  # Valid type, expected status code 200
    ]

    @allure.story("create admin panel organization")
    @allure.title("create admin panel organization test happy flow")
    @pytest.mark.parametrize("parentId, tenantId, expected_status_code, expected_error", TEST_CASES)
    def test_admin_panel_organization_post(self, access_token, parentId, tenantId, expected_status_code,
                                           expected_error):
        payload = {
            "title": "testOrg",
            "businessType": "fintech",
            "parentId": parentId,
            "tenantId": tenantId
        }
        with allure.step("create admin panel organization"):
            organizations_post = adminPanel_orgnization(access_token).create_adminPanel_orgnization(payload)
            print(organizations_post.json())
            assert organizations_post.status_code == expected_status_code
            if expected_error:
                response_json = organizations_post.json()
                assert "Details" in response_json, "Response does not contain 'Details' field"
                assert any(
                    detail["Description"] == expected_error
                    for detail in response_json["Details"]
                ), f"Expected error message '{expected_error}' not found in response: {response_json}"

    TEST_CASES = [
        # (tenant_id, page_size, expected_status_code, description)
        ("s", 1, 400, "مقدار وارد شده نا معتبر است."),
        (None, 1, 200, None),
        (8, 1, 200, None)

    ]

    @allure.story("get admin panel organization by id")
    @allure.title("get admin panel organization by id test happy flow")
    @pytest.mark.parametrize("tenant_id, page_size, expected_status_code, expected_error", TEST_CASES)
    def test_admin_panel_organization_inquiry_by_tenant(self, access_token, tenant_id, page_size, expected_status_code,
                                                        expected_error):
        with allure.step("get admin panel organization by id"):
            organization_inquiry = adminPanel_orgnization(access_token).get_adminPanel_orgnization_by_id(tenant_id)
            response_data = organization_inquiry.json()
            assert organization_inquiry.status_code == expected_status_code
            if expected_error:
                assert "Details" in response_data, "Response does not contain 'Details' field"
                assert any(
                    detail["Description"] == expected_error
                    for detail in response_data["Details"]
                ), f"Expected error message '{expected_error}' not found in response: {response_data}"

