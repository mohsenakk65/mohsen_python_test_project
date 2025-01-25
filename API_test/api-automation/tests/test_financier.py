import pytest
import json
from pages.Financier import *
from pages.tenant_page import tenantservises
from pages.token_page import *
from utils.random_values import *
from utils.helpers import validate_response, validate_schema


class TestFinancierCRUD:


    @pytest.fixture(scope="class")
    def access_token(self):
        """Fetches an access token from the token page."""
        token_response = token_page().get_token()
        return token_response.json()["accessToken"]

    @pytest.fixture(scope="class")
    def tenant_id(self, access_token):
        tenant_service = tenantservises(access_token)
        tenant_data = tenant_payload()
        response = tenant_service.create_tenant(tenant_data).json()
        return response

    @pytest.fixture(scope="class")
    def get_financier_data(self):
        """Retrieve financier data from a JSON file."""
        data = read_json_file("financierData", "DataFile/")
        return data


    @pytest.fixture(scope="class")
    def financier_data(self):
        """
        Retrieve financier data from a JSON file.

        Returns:
            dict: The financier data loaded from the JSON file.
        """
        # Read the JSON file containing financier data from the specified directory
        payload = read_json_file("financierData", "DataFile/")

        # Return the loaded data as a dictionary
        return payload






    def test_create_financier(self, access_token, tenant_id, financier_data):
        """
        Test creating a financier with valid data.
        """
        financier_data = modify_json_data(
            financier_data,
            {
                "tenantId": tenant_id,
                "name": Random_value.generate_name(10),
                "email": Random_value.generate_email(),
                "mobile": Random_value.generate_mobile_number(),
            }
        )
        response = financeiservises(access_token).Create_financier(financier_data)
        validate_response(response, 201)


    def test_get_financier_filter(self, access_token, tenant_id):
        """
        Test fetching a financier using a filter.
        """
        financier_service = financeiservises(access_token)
        response = financier_service.inquiry_financier_filter(
            tenant_id, "1", "1", page_index="1", page_size="1"
        )
        validate_response(response, 200)


    def test_get_financier_by_id(self, access_token, financier_data):
        """
        Test fetching a financier by ID.
        """
        financier_service = financeiservises(access_token)
        financier_id = financier_service.Create_financier(financier_data).json()
        response = financier_service.inquiry_financier_by_id(financier_id)
        validate_response(response, 200)


    def   test_update_financier(self, access_token, financier_data, tenant_id):
        """
        Test updating a financier with valid data.
        """
        financier_service = financeiservises(access_token)
        financier_id = financier_service.Create_financier(financier_data).json()
        financier_data = modify_json_data(
            financier_data,
            {
                "tenantId": tenant_id,
                "name": Random_value.generate_name(10),
                "email": Random_value.generate_email(),
                "mobile": Random_value.generate_mobile_number(),
            }
        )
        response = financier_service.update_financier_by_id(financier_id, financier_data)
        print(response)
        validate_response(response, 200)