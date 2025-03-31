import requests

testcases = [
    {"url": "http://localhost:8000/add/2/2", "expected": 4, "description": "Test addition of 2 and 2"},
    {"url": "http://localhost:8000/subtract/2/2", "expected": 0, "description": "Test subtraction of 2 from 2"},
    {"url": "http://localhost:8000/multiply/2/2", "expected": 4, "description": "Test multiplication of 2 and 2"}
]

def test():
    for case in testcases:
        try:
            response = requests.get(case["url"])
            response.raise_for_status()  # Raise an exception for bad status codes
            result = response.json()["result"]
            assert result == case["expected"], f"Test failed: {case['description']}. Expected {case['expected']}, got {result}"
            print(f"Test passed: {case['description']}")
        except requests.exceptions.RequestException as e:
            print(f"Test failed due to a request error: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Test failed due to response format error: {e}")
        except AssertionError as e:
            print(e)

    print("All tests passed!")

if __name__ == "__main__":
    # Start the server in a separate process for testing
    import subprocess
    import time
    server_process = subprocess.Popen(["python", "apiserver.py"])
    time.sleep(1)  # Give the server a moment to start
    try:
        test()
    finally:
        server_process.terminate()
        server_process.wait()