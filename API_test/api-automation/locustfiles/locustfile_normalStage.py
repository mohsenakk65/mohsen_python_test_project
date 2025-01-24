import logging

from locust import HttpUser, between, task, events, constant, LoadTestShape

from pages.tenant_page import tenantservises
from pages.token_page import token_page
from utils.random_values import *
from utils.configs import TENANT_URL, tenant_payload



# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("locust-test")

# Global event listeners for request success and failure
# @events.request.add_listener
# def log_request_success(request_type, name, response_time, response_length, **kwargs):
#     logger.info(f"SUCCESS: {request_type} {name} | Response time: {response_time:.2f} ms | Length: {response_length}")

# @events.request_failure
# def log_request_failure(request_type, name, response_time, exception, **kwargs):
#     print(f"FAILURE: {request_type} {name} | Response time: {response_time:.2f} ms | Exception: {exception}")


class TenantBehavior(HttpUser):
    wait_time = between(0, 2)
    token = None

    def on_start(self):
        """Fetch token at the start of the test."""
        token_page_instance = token_page()
        self.token = token_page_instance.get_token()
        if self.token:
            logger.info(f"Token fetched successfully: {self.token}")
        else:
            logger.error("Failed to fetch token.")

    @task
    def get_tenant(self):
        """Create a tenant using the fetched token."""
        if not self.token:
            logger.warning("Token not available. Skipping tenant creation.")
            return

        # payload = tenant_payload()
        tenant_service = tenantservises(self.token)
        response = tenant_service.get_tenants()

        if response:
            logger.info(f"Tenant get successful: {response}")
        else:
            logger.error("Tenant get  failed.")

class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    tasks = [TenantBehavior]


class StagesShape(LoadTestShape):
    """
    A simple load test shape class that has different user and spawn_rate at
    different stages.

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage

        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10},
        {"duration": 100, "users": 50, "spawn_rate": 10},
        {"duration": 180, "users": 100, "spawn_rate": 10},
        {"duration": 220, "users": 30, "spawn_rate": 10},
        {"duration": 230, "users": 10, "spawn_rate": 10},
        {"duration": 240, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None