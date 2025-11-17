# 13nov01

A simple Python tutorial project demonstrating how to create a web server using Flask framework with multiple endpoints.

## Project Description

This project implements a basic Flask server with two GET endpoints that return plain text responses. It serves as an educational example for learning Flask fundamentals, including:

- Setting up a Flask application
- Defining multiple route handlers
- Responding to HTTP GET requests
- Running a Python Flask server on localhost
- Writing comprehensive tests with pytest

**Note**: This project was converted from a Node.js/Express implementation to Python/Flask, preserving all original functionality.

## Prerequisites

- Python 3.11 or higher
- pip (Python Package Manager)

## Installation

1. Clone this repository or navigate to the project directory

2. Create a virtual environment (recommended):

```bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

This will install Flask and all necessary dependencies.

4. (Optional) Install test dependencies:

```bash
pip install -r requirements-test.txt
```

## Usage

Start the server by running:

```bash
python app.py
```

You should see a confirmation message indicating the server is running on `http://localhost:5000`.

## API Endpoints

The server provides the following endpoints:

### 1. Root Endpoint

- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a simple greeting message
- **Response**: `Hello world`

### 2. Evening Endpoint

- **URL**: `/evening`
- **Method**: `GET`
- **Description**: Returns an evening greeting message
- **Response**: `Good evening`

## Testing the Endpoints

You can test the endpoints using curl commands in your terminal:

### Test the root endpoint:

```bash
curl http://localhost:5000/
```

Expected output: `Hello world`

### Test the evening endpoint:

```bash
curl http://localhost:5000/evening
```

Expected output: `Good evening`

Alternatively, you can open these URLs in your web browser:
- http://localhost:5000/
- http://localhost:5000/evening

## Project Structure

```
.
├── README.md                  # This file
├── app.py                     # Main Flask server implementation
├── requirements.txt           # Production dependencies
├── requirements-test.txt      # Test dependencies
├── pytest.ini                 # pytest configuration
├── .gitignore                # Git ignore patterns
└── tests/                     # Test directory
    ├── __init__.py
    ├── conftest.py            # pytest fixtures
    └── test_server.py         # Comprehensive test suite
```

## Running Tests

This project includes a comprehensive test suite with 31 tests covering all endpoints, error handling, and edge cases.

### Run all tests:

```bash
pytest tests/ -v
```

### Run tests with coverage report:

```bash
pytest tests/ --cov=app --cov-report=term-missing
```

### Expected results:
- All 31 tests should pass
- Code coverage: 92% (exceeds 90% threshold)

## Learning Objectives

This tutorial demonstrates:
- How to initialize a Flask application
- How to define route handlers for different endpoints
- How to send text responses to HTTP requests
- How to start a Flask server and listen on a specific port
- How to write comprehensive tests with pytest
- How to measure code coverage
- How to handle errors (404, 405) properly

## Technical Details

- **Framework**: Flask 3.0.0
- **Python Version**: Python 3.11 or higher
- **Testing Framework**: pytest 7.4.3
- **Server Port**: 5000 (Flask default)
- **Content Type**: text/plain; charset=utf-8
- **Test Coverage**: 92%

## License

This is a tutorial project for educational purposes.