import pytest
import json
from pages.AdminLookupItem.AdminLookupItem import *
from pages.token_page import *
from utils.random_values import *
from utils.helpers import validate_response, validate_schema


class TestLookupItems:
    """
    test all parameters for lookup items
    """

    @pytest.fixture(scope="class")
    def access_token(self):
        accessToken = token_page().get_token()
        print(accessToken)
        token = accessToken.json()["accessToken"]
        return token

    # Define test cases for different types
    TEST_CASES = [
        (1, 200, read_json_file("type1", "Datafile/lookupitems/")),  # Valid type, expected status code 200
        (2, 200, read_json_file("type2", "Datafile/lookupitems/")),  # Valid type, expected status code 200
        (3, 200, read_json_file("type3", "Datafile/lookupitems/")),
        (4, 200, read_json_file("type4", "Datafile/lookupitems/")),
        # Invalid type, expected status code 404
    ]

    @pytest.mark.parametrize("lookup_type, expected_status_code, expected_data", TEST_CASES)


    def test_lookupItems(self, access_token, lookup_type, expected_status_code, expected_data):
        response = AdminLookup(access_token).get_lookupItems(lookup_type)
        assert response.status_code == expected_status_code, (
            f"Expected status code {expected_status_code} for type '{lookup_type}', "
            f"but got {response.status_code}"
        )
        print(response.url)

        # Optionally, print the response content for debugging
        print(f"Response for type '{lookup_type}':", response.text)