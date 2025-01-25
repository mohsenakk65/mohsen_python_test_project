def validate_response(response, expected_status_code):
    assert response.status_code == expected_status_code, f"Expected {expected_status_code}, got {response.status_code}: {response.text}"



def validate_schema(schema, data):
    """
    Validate that the given data matches the provided schema
    """
    from jsonschema import validate
    try:
        validate(instance=data, schema=schema)
    except AssertionError:
        print(f"Schema validation failed for: {data}")
        raise