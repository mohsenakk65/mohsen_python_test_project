import pytest
import json
from pages.Guarantor import *
from pages.tenant_page import tenantservises
from pages.token_page import *
from utils.random_values import *
from utils.helpers import validate_response, validate_schema


class TestGuarantorCRUD:

    @pytest.fixture(scope="class")
    def access_token(self):
        accessToken = token_page().get_token()
        token = accessToken.json()["accessToken"]
        return token


    @pytest.fixture(scope="class")
    def guarantor_data(self):
        payload = read_json_file("guarantorData", "DataFile/")
        return payload

    @pytest.fixture(scope="class")
    def tenant_id(self, access_token):
        tenant_service = tenantservises(access_token)
        tenant_data = tenant_payload()
        response = tenant_service.create_tenant(tenant_data).json()
        return response



    def test_create_guarantor(self, access_token, guarantor_data, tenant_id):
        data = modify_json_data(guarantor_data, {"tenantId": tenant_id, "individual.email": Random_value.generate_email(), "individual.mobile": Random_value.generate_mobile_number(), "individual.birthDate": Random_value.generate_random_date(start_date='1950-11-19T07:21:03.314', end_date='2022-11-19T07:21:03.314') , "legal.establishmentDate": Random_value.generate_random_date(start_date='1950-11-19T07:21:03.314', end_date='2022-11-19T07:21:03.314')})
        guarantor_service = GuarantorCRUD(access_token).create_guarantor(data)
        print(guarantor_service)
        validate_response(guarantor_service, 201)



    def test_get_guarantor_filter(self, access_token, tenant_id):
        guarantor_service = GuarantorCRUD(access_token)
        DATA = guarantor_service.inquiry_guarantor_by_filter(tenantId=tenant_id, LegalTypeId=1, PersonType=1)
        validate_response(DATA, 200)
        print(DATA)


    def test_get_guarantor_by_id(self, access_token, tenant_id, guarantor_data):
        data = modify_json_data(guarantor_data, {"tenantId": tenant_id, "individual.email": Random_value.generate_email(), "individual.mobile": Random_value.generate_mobile_number(), "individual.birthDate": Random_value.generate_random_date(start_date='1950-11-19T07:21:03.314', end_date='2022-11-19T07:21:03.314') , "legal.establishmentDate": Random_value.generate_random_date(start_date='1950-11-19T07:21:03.314', end_date='2022-11-19T07:21:03.314')})

        guarantorId = GuarantorCRUD(access_token).create_guarantor(data).json()
        guarantor_service = GuarantorCRUD(access_token)
        response  = guarantor_service.inquary_guarantor_by_id(guarantorId)
        validate_response(response, 200)

    def test_update_guarantor(self, access_token,guarantor_data, tenant_id ):
        data = modify_json_data(guarantor_data,
                                {"tenantId": tenant_id, "individual.email": Random_value.generate_email(),
                                 "individual.mobile": Random_value.generate_mobile_number(),
                                 "individual.birthDate": Random_value.generate_random_date(
                                     start_date='1950-11-19T07:21:03.314', end_date='2022-11-19T07:21:03.314'),
                                 "legal.establishmentDate": Random_value.generate_random_date(
                                     start_date='1950-11-19T07:21:03.314', end_date='2022-11-19T07:21:03.314')})

        guarantorId = GuarantorCRUD(access_token).create_guarantor(data).json()
        updated_data = modify_json_data(guarantor_data, {"individual.email": Random_value.generate_email(),
                                 "individual.mobile": Random_value.generate_mobile_number(),
                                 "individual.birthDate": Random_value.generate_random_date(
                                     start_date='1950-11-19T07:21:03.314', end_date='2022-11-19T07:21:03.314')})

        updated_guarantor  = GuarantorCRUD(access_token).update_guarantor_by_id(guarantorId, updated_data)
        validate_response(updated_guarantor, 200)










