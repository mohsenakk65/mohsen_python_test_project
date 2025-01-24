Feature: Tenant Management API
  As a system user
  I want to manage tenants via API
  So that I can automate tenant operations

  Scenario: Create a new tenant successfully
    Given I have a valid authentication token
    When I send a POST request to create a tenant with valid data
    Then the response status code should be 201
    And the response body should contain the tenant ID

  Scenario: Create a tenant with invalid data
    Given I have a valid authentication token
    When I send a POST request to create a tenant with invalid data
    Then the response status code should be 400
