import allure
import pytest
import json
from pages.AdminCustomer.AdminCustomer import admin_Customer
from pages.tenant_page import tenantservises
from pages.token_page import token_page
from utils.random_values import *
from pages.AdminOrgnization.adminpanelOrganizations import adminPanel_orgnization
from utils.helpers import validate_response, validate_schema
from utils.configs import *


@allure.suite("Admin Customer CRUD Operations")
class TestAdminCustomer:
    """
    Test suite for Admin Customer CRUD operations.
    """

    @pytest.fixture(scope="class")
    def access_token(self):
        """
        Fixture to get the access token for API authentication.
        """
        access_token_response = token_page().get_token()
        assert access_token_response.status_code == 200, "Failed to fetch access token"
        print(access_token_response.json()["accessToken"])

        return access_token_response.json()["accessToken"]

    @pytest.fixture(scope="class")
    def tenant_id(self, access_token):
        """
        Fixture to create a tenant and return its ID.
        """
        tenant_service = tenantservises(access_token)
        tenant_data = tenant_payload()
        response = tenant_service.create_tenant(tenant_data)
        print(response.json())
        assert response.status_code == 201, "Failed to create tenant"
        return response.json()

    @pytest.fixture(scope="class")
    def organization_id(self, tenant_id, access_token):
        """
        Fixture to create an organization and return its ID.
        """
        payload = {
            "title": "testOrg",
            "businessType": "fintech",
            "parentId": None,
            "tenantId": tenant_id
        }
        response = adminPanel_orgnization(access_token).create_adminPanel_orgnization(payload)
        assert response.status_code == 201, f"Failed to create organization with incorrect status_code  {response.status_code}"
        print(response.json())
        return response.json()

    @allure.story("Create Admin Customer")
    @allure.title("Test Admin Customer Creation")
    def test_admin_panel_customer_creation(self, tenant_id, access_token, organization_id):
        """
        Test case to validate the creation of an admin customer.
        """
        # Read and modify JSON payload
        raw_data = read_json_file("AdminPanelCustomer", "DataFile/")
        payload = modify_json_data(raw_data, {
            "tenantId": tenant_id,
            "organizationId": organization_id,
            "nationalId": "3934466842",
            "fatherName": "تقی",
            "firstName": "محسن",
            "lastName": "اکبری",
            "gender": 1,
            "birthPlace": "tehran",
            "cityId": "1",
            "address": "شهر تبریز، خیابان بهشتی، مجتمع پارسیان، پلاک 131، طبقه 7",
            "postalCode": "1647878515",
            "email": "m.akbari@gmail.com",
            "certificateNumber": "102030",
            "birthDate": "2000-12-18T01:44:47.886Z",
            "mobile": "09184417118",
            "tel": "02177192918",
            "description": "test"
        })

        with allure.step("Call Admin Customer API to create customer"):
            response = admin_Customer(access_token).get_create_customer(payload)

            # Log the request and response in Allure
            allure.attach(json.dumps(payload, indent=4), name="Request Payload", attachment_type=allure.attachment_type.JSON)
            allure.attach(json.dumps(response.json(), indent=4), name="Response", attachment_type=allure.attachment_type.JSON)

            if response.status_code == 400:
                # Handle 400 Bad Request error
                error_message = response.json().get("Details", "Unknown error")
                allure.attach(str(error_message), name="Error Details", attachment_type=allure.attachment_type.TEXT)
                pytest.fail(f"API returned 400 Bad Request: {error_message}")
            else:
                # Validate successful response
                validate_response(response, 201)

    @allure.title("Test Admin Customer Update")
    @allure.story("Update Admin Customer")
    def test_admin_panel_customer_inquiry(self, tenant_id, access_token, organization_id):
        """
        Test case to validate the update of an admin customer.
        """
        with    allure.step("inquiry_customer API"):
            response = admin_Customer(access_token).get_customer_by_id(organization_id)

            # Log the request and response in Allure
            allure.attach(json.dumps(response.json(), indent=4), name="Response", attachment_type=allure.attachment_type.JSON)

            if response.status_code == 400:
                # Handle 400 Bad Request error

                error_message = response.json().get("Details", "Unknown error")
                allure.attach(str(error_message), name="Error Details", attachment_type=allure.attachment_type.TEXT)
                pytest.fail(f"API returned 400 Bad Request: {error_message}")
            else:
                # Validate successful response
                validate_response(response, 200)
    @allure.story("test_admin panel _customer_inquiry")
    @allure.title("admin panel custumer inquiry")
    def test_admin_panel_inquiry(self, tenant_id, access_token, organization_id):
        """
        Test case to validate the update of an admin customer.
        """
        with    allure.step("inquiry_customer API"):
            response = admin_Customer(access_token).get_customer_by_id(organization_id)

            # Log the request and response in Allure
            allure.attach(json.dumps(response.json(), indent=4), name="Response", attachment_type=allure.attachment_type.JSON)

            if response.status_code == 400:
                # Handle 400 Bad Request error

                error_message = response.json().get("Details", "Unknown error")
                allure.attach(str(error_message), name="Error Details", attachment_type=allure.attachment_type.TEXT)
                pytest.fail(f"API returned 400 Bad Request: {error_message}")
            else:
                # Validate successful response
                validate_response(response, 200)

