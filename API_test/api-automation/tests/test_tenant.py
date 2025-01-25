import pytest
import json
from pages.tenant_page import *
from pages.token_page import *
from utils.random_values import *
from utils.helpers import validate_response, validate_schema


class TestTenantCRUD:
    """
    Test class for Tenant CRUD operations.
    """

    @pytest.fixture(scope="class")

    def tenant_data(self):
        return tenant_payload()

    @pytest.fixture(scope="class")
    def access_token(self):
        accessToken = token_page().get_token()
        print(accessToken)
        token = accessToken.json()["accessToken"]
        return token

    @pytest.fixture(scope="function")
    def rollBackTenant(self):
        """
        Fixture to delete a tenant from the database after each test.
        """

        def _delete_tenant(tenant_id):
            with establish_connection() as db_connection:
                # Use a parameterized query to avoid SQL injection
                query = "DELETE FROM ClientManagement.client.Tenant WHERE id = ?;"
                execute_query(db_connection, query, (tenant_id, ))

        return _delete_tenant

    @pytest.mark.run(order=1)
    def test_create_tenant(self, access_token, tenant_data, rollBackTenant):
        """
        Test case for creating a tenant.

        Args:
            access_token (str): The access token.
            tenant_data (dict): The payload for tenant creation.
        """
        tenant_service = tenantservises(access_token)
        response = tenant_service.create_tenant(tenant_data)
        print(response)
        # validate_response(response, 201)
        assert response.status_code == 201
        #roolbak data from database
        # rollBackTenant(response.json())

    @pytest.mark.run(order=1)
    def test_get_tenants(self, access_token):
        tenant_service = tenantservises(access_token)
        response = tenant_service.get_tenants()

        assert response.status_code == 200

    def test_update_tenant(self, access_token, tenant_data ):
        tenant_id = tenantservises(access_token).create_tenant(payload=tenant_data).json()
        # update_payload = read_json_file("AdminPanelTenant", "DataFile/")
        modified_payload = modify_json_data(tenant_data, {"creditProjectName": "کیف پول انتخاب",

                                                                        "tenantName": "mohsen"
                                                                          })
        print(modified_payload)

        update_response = tenantservises(access_token).update_tenant(payload=modified_payload, tenantId=tenant_id)

        print(update_response.json())
        assert update_response.status_code == 200

    @pytest.mark.run(order=1)
    def test_get_tenant_by_id(self, access_token, tenant_data):
        # Debug: Print the access token to verify it's correct
        print("Access Token:", access_token)

        # Step 1: Create a tenant and get the tenant ID
        tenant_service = tenantservises(access_token)
        tenant_id = tenant_service.create_tenant(tenant_data).json()
        print("Created Tenant ID:", tenant_id)

        # Step 2: Fetch the tenant details by ID
        response = tenant_service.get_tenants_by_id(tenant_id)
        print("Response Status Code:", response.status_code)
        print("Response Body:", response.json())

        # Step 3: Validate the response
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"





