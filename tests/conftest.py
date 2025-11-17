"""
pytest configuration and fixtures for Flask application testing.

This module provides shared fixtures that are automatically discovered by pytest
and can be used across all test files.
"""

import pytest
from app import app as flask_app


@pytest.fixture
def app():
    """
    Create and configure a Flask application instance for testing.
    
    Yields:
        Flask: Configured Flask application instance with TESTING=True
    """
    flask_app.config['TESTING'] = True
    yield flask_app


@pytest.fixture
def client(app):
    """
    Create a test client for making HTTP requests to the Flask application.
    
    Args:
        app: Flask application fixture
        
    Returns:
        FlaskClient: Test client for making requests
    """
    return app.test_client()


@pytest.fixture
def app_context(app):
    """
    Provide an application context for tests that need it.
    
    Args:
        app: Flask application fixture
        
    Yields:
        ApplicationContext: Active application context
    """
    with app.app_context():
        yield
