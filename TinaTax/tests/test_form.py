import pytest
from utils.csv_reader import load_form

# Each row from the CSV becomes a separate test case
@pytest.mark.parametrize("row", load_form())
def test_post_form(form_api, row):
    expected_status = row["expected_status"]
    payload = {k: v for k, v in row.items() if k != "expected_status"}  # don't send expected_status to server
    response = form_api.post_form(payload)

    # Check status code
    assert response.status_code == expected_status, (
        f"Expected status {expected_status}, got {response.status_code}"
    )

    # Check response body confirms the form was received
    if expected_status == 200:
        body = response.json()
        assert body.get("ok") is True, f"Expected ok=true in response, got: {body}"
        assert isinstance(body.get("message"), str), f"Expected message to be a string, got: {body}"
        assert body["message"].strip(), "Expected message to not be empty"
