# FastAPI Backend with Automated Testing

This project is a simple FastAPI backend that provides basic mathematical operations (addition, subtraction, multiplication) and includes automated tests written using `pytest`. It also demonstrates basic API key authentication for a secured endpoint.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the FastAPI Server](#running-the-fastapi-server)
- [Running the Tests](#running-the-tests)
- [API Endpoints](#api-endpoints)
- [API Key Authentication](#api-key-authentication)
- [GitHub Actions](#github-actions)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python:** Version 3.8 or higher (check with `python --version` or `python3 --version`)
- **pip:** Python package installer (usually comes with Python)
- **Git:** Version control system (check with `git --version`)
- **GitHub Account:** For storing your project and using GitHub Actions.

## Setup

1.  **Clone the Repository (if you haven't already):**
    ```bash
    git clone <your_repository_url>
    cd fastapi_testing
    ```
    (Replace `https://github.com/i-lakshay/FastAPI-backend.git` with the URL of your GitHub repository)

2.  **Create a Virtual Environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (You'll need to create a `requirements.txt` file first. See the next step.)

4.  **Create `requirements.txt`:**
    To easily install all the necessary packages, create a file named `requirements.txt` in your project root and add the following lines:
    ```
    fastapi
    uvicorn
    requests
    pytest
    ```
    Then, run the installation command from step 3.

## Running the FastAPI Server

1.  **Activate your virtual environment** (if you haven't already).
2.  Navigate to the project root directory in your terminal.
3.  Run the FastAPI server using Uvicorn:
    ```bash
    python apiserver.py
    ```
    The server will start at `http://localhost:8000`. You can then access the API endpoints in your web browser or using tools like `curl`.

## Running the Tests

1.  **Activate your virtual environment** (if you haven't already).
2.  Navigate to the project root directory in your terminal.
3.  Run the pytest test suite:
    ```bash
    pytest testAutomationPytest.py
    ```
    Pytest will discover and run all the test functions in the `testAutomationPytest.py` file, reporting the results in your terminal.

## API Endpoints

-   **`/` (GET):** Returns a simple greeting: `{"Hello": "World"}`.
-   **`/add/{num1}/{num2}` (GET):** Adds two numbers and returns the result: `{"result": <sum>}`.
-   **`/subtract/{num1}/{num2}` (GET):** Subtracts the second number from the first and returns the result: `{"result": <difference>}`.
-   **`/multiply/{num1}/{num2}` (GET):** Multiplies two numbers and returns the result: `{"result": <product>}`.
-   **`/operations/` (GET):** Returns a list of all performed operations stored in the database.
-   **`/secure/data` (GET):** A secured endpoint that requires a valid API key in the `X-API-Key` header to access. Returns `{"message": "This data is secured!"}` if authenticated.

## API Key Authentication

The `/secure/data` endpoint is protected by basic API key authentication.

-   **Valid API Key:** The server checks for an `X-API-Key` header in the request. A valid API key is defined in the `API_KEYS` list within the `apiserver.py` file (currently `["your_secret_api_key"]`).
-   **Unauthorized Access:** If the `X-API-Key` header is missing or contains an invalid key, the server will return a `401 Unauthorized` status code with the detail `"Invalid API Key"`.

**Note:** For production applications, it is highly recommended to store and manage API keys more securely than hardcoding them in the application code. Consider using environment variables, configuration files, or dedicated secret management systems.

## GitHub Actions

This project includes a GitHub Actions workflow (`.github/workflows/test.yml`) that automatically runs the pytest tests whenever code is pushed to the `main` branch or a pull request is created targeting the `main` branch.

-   The workflow sets up a Python environment, installs dependencies, starts the FastAPI server, waits for it to be ready, and then executes the pytest tests.
-   You can view the status of these automated tests in the "Actions" tab of your GitHub repository.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature` or `git checkout -b bugfix/your-fix`).
3.  Make your changes and commit them (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/your-feature`).
5.  Create a new Pull Request on GitHub.

## License

["Not currently Licenced"]

---