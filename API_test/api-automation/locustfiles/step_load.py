import math

from locust import HttpUser, LoadTestShape, TaskSet, constant, task
from locust import HttpUser, task, between, events, LoadTestShape
import logging

from locustfiles.locustfile import logger
from pages.tenant_page import tenantservises
from pages.token_page import token_page
from utils.random_values import *
from utils.configs import TENANT_URL, tenant_payload



import math


class UserTasks(TaskSet):
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
    def get_root(self):
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
    tasks = [UserTasks]


class StepLoadShape(LoadTestShape):
    """
    A step load shape


    Keyword arguments:

        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds

    """

    step_time = 30
    step_load = 10
    spawn_rate = 10
    time_limit = 600

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return current_step * self.step_load, self.spawn_rate