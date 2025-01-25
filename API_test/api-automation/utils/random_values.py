import random
import string
from datetime import datetime, timedelta

import pytest


class Random_value:
    @staticmethod
    def generate_random_national_code():
        """Generate a random 10-digit national code."""
        return ''.join(str(random.randint(0, 9)) for _ in range(10))

    @staticmethod
    def generate_random_date(start_date, end_date):
        """Generate a random ISO 8601 date between start_date and end_date."""
        start = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S.%f")
        end = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S.%f")
        random_date = start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
        return random_date.isoformat() + "Z"

    @staticmethod
    def generate_phone_number():
        """Generate a random phone number matching the pattern ^0[0-9]{2,}[0-9]{7,}$."""
        prefix = "0"
        middle_part = ''.join(str(random.randint(0, 9)) for _ in range(random.randint(2, 4)))
        last_part = ''.join(str(random.randint(0, 9)) for _ in range(random.randint(7, 10)))
        return prefix + middle_part + last_part

    @staticmethod
    def generate_name(length):
        """Generate a random name using Farsi and English characters."""
        farsi_letters = "ابتثجحخدذرزسشصضطظعغفقکلمنهوية"
        english_letters = string.ascii_letters
        allowed_chars = farsi_letters + english_letters + " "
        name = ''.join(random.choice(allowed_chars) for _ in range(length)).strip()
        return name if len(name) >= 2 else Random_value.generate_name(length)

    @staticmethod
    def generate_email():
        """Generate a random email address."""
        name = Random_value.generate_name(10)
        domain = "example.com"
        return f"{name}@{domain}"


    @staticmethod
    def generate_postal_code():
        """Generate a random 10-digit postal code matching the pattern."""
        while True:
            first_part = ''.join(random.choice("13456789") for _ in range(4))
            if not any(first_part.count(digit) == 4 for digit in "0123456789"):
                break
        fifth_digit = random.choice("1346789")
        last_part = ''.join(random.choice("013456789") for _ in range(5))
        return first_part + fifth_digit + last_part

    @staticmethod
    def generate_mobile_number():
        """Generate a mobile number starting with 091."""
        prefix = "091"
        return prefix + ''.join(str(random.randint(0, 9)) for _ in range(8))

    @staticmethod

    def generate_farsi_address():

        """Generate farsi random address"""
        city_names = ["تهران", "مشهد", "اصفهان", "شیراز", "تبریز", "کرج", "اهواز"]
        street_names = ["ولیعصر", "مطهری", "بهشتی", "آزادی", "انقلاب", "فردوسی", "امام خمینی"]
        building_names = ["ساختمان امید", "برج میلاد", "مجتمع بهار", "ساختمان نور", "مجتمع پارسیان"]

        # Generate a random Farsi address
        random_city = random.choice(city_names)
        random_street = random.choice(street_names)
        random_building = random.choice(building_names)
        random_building_number = random.randint(1, 200)  # Random building number between 1 and 200
        random_floor = random.randint(1, 10)
        random_address = f"شهر {random_city}، خیابان {random_street}، {random_building}، پلاک {random_building_number}، طبقه {random_floor}"
        return random_address

    @staticmethod

    def generate_lastname():

        """Genarate last name randomly"""

        last_names = ["اکبری", "رستمی", "حسینی", "رضایی", "محمدی", "علوی", "شعبانی"]
        random_last_name = random.choice(last_names)
        print("Generated Last Name:", random_last_name)
        return random_last_name

    @pytest.fixture()
    def tenant_payload(self):
        """
        Pytest fixture to generate a tenant payload with random values.

        Returns:
            dict: A dictionary containing tenant data.
        """
        first_name = Random_value.generate_name(10)
        last_name = Random_value.generate_lastname()
        national_id = Random_value.generate_random_national_code()
        birth_date = Random_value.generate_random_date(
            start_date="1901-11-19T07:21:03.314",
            end_date="2022-11-19T07:21:03.314",
        )
        mobile_number = Random_value.generate_mobile_number()
        address = Random_value.generate_farsi_address()
        postal_code = Random_value.generate_postal_code()
        establishment_date = Random_value.generate_random_date(
            start_date="2000-11-19T07:21:03.314",
            end_date="2024-11-19T07:21:03.314",
        )

        return {
            "ownerName": "کیپا",
            "brandName": "کیپا",
            "description": "test",
            "creditProjectName": "کیف پول کیپا",
            "identityType": 1,
            "individual": {
                "firstName": first_name,
                "lastName": last_name,
                "nationalId": national_id,
                "birthDate": birth_date,
                "mainMobileNumber": mobile_number,
                "fullAddress": address,
                "postalCode": postal_code,
            },
            "legal": {
                "name": "گروه کیپا",
                "nationalId": "11111111111",
                "establishmentDate": establishment_date,
                "registrationNumber": "3934466842",
                "legalTypeId": 1,
                "fullAddress": address,
                "postalCode": postal_code,
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
