from locust import HttpUser, task, between, events, LoadTestShape
import logging
from pages.tenant_page import tenantservises
from pages.token_page import token_page
from utils.random_values import *
from utils.configs import TENANT_URL, tenant_payload

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("locust-test")

# Global event listeners for request success and failure
@events.request.add_listener
def log_request_success(request_type, name, response_time, response_length, **kwargs):
    logger.info(f"SUCCESS: {request_type} {name} | Response time: {response_time:.2f} ms | Length: {response_length}")

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
    def create_tenant(self):
        """Create a tenant using the fetched token."""
        if not self.token:
            logger.warning("Token not available. Skipping tenant creation.")
            return

        payload = tenant_payload()
        tenant_service = tenantservises(self.token)
        response = tenant_service.create_tanant(payload)

        if response:
            logger.info(f"Tenant creation successful: {response}")
        else:
            logger.error("Tenant creation failed.")


class DoubleWaveLoadShape(LoadTestShape):
    """
    Load test shape with two ramps and peaks:
    - First ramp-up: 1 -> 50 users in 5 minutes
    - First ramp-down: 50 -> 10 users in 3 minutes
    - Second ramp-up: 10 -> 100 users in 7 minutes
    - Second ramp-down: 100 -> 1 user in 5 minutes
    """
    stages = [
        {"duration": 300, "users": 50, "spawn_rate": 10},  # Ramp-up to 50 users over 5 minutes
        {"duration": 480, "users": 10, "spawn_rate": 15},  # Ramp-down to 10 users over 3 minutes
        {"duration": 900, "users": 100, "spawn_rate": 20},  # Ramp-up to 100 users over 7 minutes
        {"duration": 1200, "users": 1, "spawn_rate": 20},   # Ramp-down to 1 user over 5 minutes
    ]

    def tick(self):
        """Determine the current user load based on the elapsed time."""
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                return stage["users"], stage["spawn_rate"]
        return None
