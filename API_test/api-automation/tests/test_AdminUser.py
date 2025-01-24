import pytest
import json
from pages.AdminUser.AdminUser import *
from pages.token_page import *
from utils.random_values import *
from utils.helpers import validate_response, validate_schema


class TestAdminUser:
    """
    in this test spase we want validat all criteria in admin panel user

    """


    @pytest.fixture(scope="class")
    def access_token(self):
        accessToken = token_page().get_token()
        print(accessToken)
        token = accessToken.json()["accessToken"]
        return token

    @pytest.fixture(scope="class")
    def user_data(self):
        payload = read_json_file("AdminUserData", "DataFile/")
        return payload

    # Define test cases
    TEST_CASES = [
        # Test case 1: Valid data, expected status 200
        (
            modify_json_data(read_json_file("AdminUserData", "DataFile/"), {
                "email": Random_value.generate_email(),
                "mobileNumber": Random_value.generate_mobile_number()
            }),
            200, None
        ),
        # Test case 2: Invalid email, expected status 400
        (
            modify_json_data(read_json_file("AdminUserData", "DataFile/"), {
                "email": "Merlin_Crist55@gmail.com",  # Invalid email format
                "mobileNumber": Random_value.generate_mobile_number()
            }),
            400,"ایمیل وارد شده تکراری است."
        ),

         # tast case 3 incorrect mobile number
        ( modify_json_data(read_json_file("AdminUserData", "DataFile/"),{
                "email": Random_value.generate_email(),  # Invalid email format
                "mobileNumber": "09333974776"
            }),
            400, "شماره موبایل تکراری است.")
    ]

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("json_data, expected_status_code, expected_error_message", TEST_CASES)

    def test_get_admin_user_create_users(self, access_token, json_data, expected_status_code, expected_error_message):
#         json_data = modify_json_data(user_data, {"email": Random_value.generate_email() , "password": "@Mo123456",     "mobileNumber":Random_value.generate_mobile_number() ,
# })
        admin_user = AdminUser(access_token)
        response = admin_user.get_create_user(payload=json_data)
        print(response)
        assert response.status_code == expected_status_code, f"Expected status code 200, but got {response.status_code}"
        if expected_error_message:
            response_json = response.json()
            assert "Details" in response_json, "Response does not contain 'Details' field"
            assert any(
                detail["Description"] == expected_error_message
                for detail in response_json["Details"]
            ), f"Expected error message '{expected_error_message}' not found in response: {response_json}"

            # Optionally, print the response for debugging
        print(f"Response for JSON data {json_data}:", response.text)


    @pytest.mark.run(order=2)
    def test_get_admin_user_inquiryUsers(self, access_token):
        admin_user = AdminUser(access_token)
        response = admin_user.get_admin_users()

        assert response.status_code == 200 , f"Expected status code 200, but got {response.status_code} and response is {response.json()}"


    @pytest.mark.run(order=3)
    def test_get_adminUser_internalProject_manager(self, access_token):
        admin_user = AdminUser(access_token)
        response = admin_user.get_user_internal_projectmanagers()
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code} and response is {response.json()}"

    @pytest.mark.run(order=4)
    def test_get_adminUser_by_user_entitytypes(self, access_token):
        admin_user = AdminUser(access_token)
        response = admin_user.get_user_by_user_entitytypes()
        validate_response(response, 200)
        # assert response.status_code == 200, f"Expected status code 200, but got {response.status_code} and response is {response.json()}"