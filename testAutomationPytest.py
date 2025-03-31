import pytest
import requests
import json

BASE_URL = "http://localhost:8000"

testcases = [
    (f"{BASE_URL}/add/2/2", 4, "Test addition of 2 and 2"),
    (f"{BASE_URL}/subtract/2/2", 0, "Test subtraction of 2 from 2"),
    (f"{BASE_URL}/multiply/2/2", 4, "Test multiplication of 2 and 2"),
    (f"{BASE_URL}/add/-1/1", 0, "Test addition of -1 and 1"),
    (f"{BASE_URL}/multiply/0/5", 0, "Test multiplication by zero"),
]

@pytest.fixture(scope="module", autouse=True)
def server():
    """Fixture to start and stop the FastAPI server."""
    import subprocess
    import time
    process = subprocess.Popen(["python", "apiserver.py"])
    time.sleep(1)  # Wait for the server to start
    yield
    process.terminate()
    process.wait()

@pytest.mark.parametrize("url, expected, description", testcases)
def test_api(url, expected, description):
    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.json().get("result")
        assert result == expected, f"{description}. Expected {expected}, got {result}"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request error: {e}")
    except (KeyError, json.JSONDecodeError):
        pytest.fail("Invalid JSON response or missing 'result' key")
    except AssertionError as e:
        pytest.fail(str(e))