import json
import os

import pyodbc
from contextlib import contextmanager

from utils.random_values import Random_value
BASE_URL = "http://31.214.173.200:1000/bff"

TOKEN_URL = f"{BASE_URL}:8080/connect/token"
TENANT_URL = f"{BASE_URL}:8080/client-managements/admin-panel/tenants"

CLIENT_ID = "test-user"
CLIENT_SECRET = "secret_9e8bfc67c933a386ddb5fa5f4669227085db904d2d0a196793a802289c0d2665"
SCOPE = "keepa_identity_admin_api"

TenantPrefixCode = "10000",
USERNAME = "09125971157",
PASSWORD = "Pass123$50"


def tenant_payload():
    firstName = Random_value.generate_name(10)
    lastName = Random_value.generate_lastname()
    nationalId = Random_value.generate_random_national_code()
    birthDate = Random_value.generate_random_date(start_date='1901-11-19T07:21:03.314',
                                                  end_date='2022-11-19T07:21:03.314')
    mobileNumber = Random_value.generate_mobile_number()
    Adderss = Random_value.generate_farsi_address()
    postalCode = Random_value.generate_postal_code()
    establishmentDate = Random_value.generate_random_date(start_date='2000-11-19T07:21:03.314',
                                                          end_date='2024-11-19T07:21:03.314')



    return {
        "ownerName": "کیپا",
        "brandName": "کیپا",
        "description": "test",
        "creditProjectName": "کیف پول کیپا",
        "identityType": 1,
        "individual": {
            "firstName": firstName,
            "lastName": lastName,
            "nationalId": nationalId,
            "birthDate": birthDate,
            "mainMobileNumber": mobileNumber,
            "fullAddress": Adderss,
            "postalCode": postalCode,
        },
        "legal": {
            "name": "گروه کیپا",
            "nationalId": "11111111111",
            "establishmentDate": establishmentDate,
            "registrationNumber": "3934466842",
            "legalTypeId": 1,
            "fullAddress": Adderss,
            "postalCode": postalCode,
        },
        "ownerConnectors": [
            {
                "positionId": 17,
                "firstName": "محسن",
                "lastName": "اکبری قره باغی",
                "mobiles": ["09184417118"],
                "phones": [],
                "emails": [],
                "description": "string",
            }
        ],
        "ownerAgents": [
            {
                "positionId": 23,
                "firstName": "مجید",
                "lastName": "سفیداری",
                "nationalId": "4911764082",
                "mobiles": ["09125971158"],
                "phones": [],
                "emails": [],
            }
        ],
        "roleIds": [2],
    }


def dev_url_maker(url2nt, end_point):
    """Generate a URL based on the given end point"""
    base_url = "http://31.214.173.200:1000/bff"

    return f"{base_url}/{url2nt}/{end_point}"

def DEV_TOKEN_URL(end_point):
    baseUrl = "http://31.214.173.200:1000/bff"
    return f"{baseUrl}/{end_point}"




def     financier_payload(tenant_id):
    firstName = Random_value.generate_name(10)
    lastName = Random_value.generate_lastname()
    nationalId = Random_value.generate_random_national_code()
    birthDate = Random_value.generate_random_date(start_date='1901-11-19T07:21:03.314', end_date='2022-11-19T07:21:03.314')
    mobileNumber = Random_value.generate_mobile_number()
    Adderss = Random_value.generate_farsi_address()
    postalCode=  Random_value.generate_postal_code()
    establishmentDate = Random_value.generate_random_date(start_date='2000-11-19T07:21:03.314', end_date='2024-11-19T07:21:03.314')
    name = Random_value.generate_name(4)



    return {
  "name": name,
  "tenantId":tenant_id ,
  "personType": 2,
  "individual": {
    "firstName": firstName,
    "lastName": lastName,
    "nationalId": nationalId,
    "birthDate": birthDate,
    "mobile": mobileNumber
  },
  "legal": {
    "legalTypeId": 1,
    "name": name,
    "nationalId": "80011110011",
    "establishmentDate": establishmentDate,
    "registrationNumber": "10"
  },
  "address": Adderss,
  "postalCode": postalCode,
  "description": "تست",
  "financierAgents": [
    {
      "positionName": "صندوقدار",
      "firstName": "تامین کننده",
      "lastName": lastName,
      "nationalId": "8632110004",
      "mobile": "09121152460",
      "email": "test@gmail.com",
      "phone": "09120001456"
    }
  ],
  "financierConnectors": [
     {
      "firstName": "ایمان",
      "lastName": "شیخ",
      "nationalId": "7864119700",
      "mobile": "09150011101",
      "email": "i.sheikh@gmail.com",
      "phone": "09129998818"
    }
  ]
}


def read_json_file(file_name, directory):
    """
        Read a JSON file and return the data as a dictionary.

        Args:
            file_name (str): The name of the JSON file (without the .json extension).
            directory (str): The directory where the JSON file is located. Default is "test_data".

        Returns:
            dict: The data from the JSON file.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
    # Construct the file path
    file_path = os.path.join(directory, f"{file_name}.json")

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Read and parse the JSON file
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def modify_json_data(data, modifications):
    """
    Update the JSON data with the given modifications.
    Handles both flat keys (e.g., "email") and nested keys (e.g., "individual.firstName").
    """
    for key, value in modifications.items():
        # Split the key into parts (e.g., "individual.firstName" -> ["individual", "firstName"])
        keys = key.split(".")

        # Traverse the JSON data to find the target field
        current = data
        for k in keys[:-1]:  # Navigate to the parent of the target field
            if isinstance(current, dict):
                current = current.setdefault(k, {})  # Use setdefault to create nested dictionaries if needed
            elif isinstance(current, list):
                try:
                    index = int(k)
                    current = current[index]
                except (ValueError, IndexError):
                    raise KeyError(f"Invalid key path: {key}")
            else:
                raise KeyError(f"Invalid key path: {key}")

        # Update the target field
        last_key = keys[-1]
        if isinstance(current, dict):
            current[last_key] = value
        elif isinstance(current, list):
            try:
                index = int(last_key)
                current[index] = value
            except (ValueError, IndexError):
                raise KeyError(f"Invalid key path: {key}")
        else:
            raise KeyError(f"Invalid key path: {key}")

    return data
# def modify_json_data(data, modifications):
#
#
#     for key, value in modifications.items():
#         # Split the key into parts (e.g., "individual.firstName" -> ["individual", "firstName"])
#         keys = key.split(".")
#
#         # Traverse the JSON data to find the target field
#         current = data
#         for k in keys[:-1]:  # Navigate to the parent of the target field
#             if isinstance(current, dict):
#                 current = current.get(k, {})
#             elif isinstance(current, list):
#                 try:
#                     index = int(k)
#                     current = current[index]
#                 except (ValueError, IndexError):
#                     raise KeyError(f"Invalid key path: {key}")
#             else:
#                 raise KeyError(f"Invalid key path: {key}")
#
#         # Update the target field
#         last_key = keys[-1]
#         if isinstance(current, dict):
#             current[last_key] = value
#         elif isinstance(current, list):
#             try:
#                 index = int(last_key)
#                 current[index] = value
#             except (ValueError, IndexError):
#                 raise KeyError(f"Invalid key path: {key}")
#         else:
#             raise KeyError(f"Invalid key path: {key}")
#
#     return data

# Establish connection



@contextmanager
def establish_connection():
    host = '31.214.173.200'
    port = '1433'
    user = 'sa'
    password = 'VO2v!A7h#rtj'
    database = 'ClientManagement'
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={host},{port};DATABASE={database};UID={user};PWD={password}'

    # Establish the connection
    connection = pyodbc.connect(connection_string)
    try:
        yield connection  # Yield control back to the block under the 'with'
    finally:
        connection.close()  # Ensure the connection is closed when done


# Query execution function
def execute_query(connection, query, params=None):

    cursor = connection.cursor()

    try:
        # Execute the query with parameters
        cursor.execute(query, params or ())

        # Fetch results only for SELECT queries
        if query.strip().lower().startswith("select"):
            results = cursor.fetchall()
        else:
            results = None

        # Commit the transaction for write operations
        if not query.strip().lower().startswith("select"):
            connection.commit()

        return results
    except Exception as e:
        # Rollback the transaction in case of error
        connection.rollback()
        raise e

    finally:
        # Close the cursor
        cursor.close()


# Function for test connection
# def test_connection():
#     with establish_connection() as connection:
#         query = "SELECT x.* FROM ClientManagement.client.LookupItem AS x WHERE Id = 7"
#         results = execute_query(connection, query)
#         print(results)
#         assert results

    # Run the test connection function to check if everything is working


# if __name__ == "__main__":
#     test_connection()