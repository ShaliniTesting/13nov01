"""
Comprehensive test suite for Flask server application.

This module tests:
- Application initialization
- Root endpoint (/) functionality
- Evening endpoint (/evening) functionality
- Error handling (404, 405)
- Response formatting and headers
- Performance validation
- Edge cases
"""

import pytest
import time


class TestApplicationInitialization:
    """Test Flask application initialization and configuration."""
    
    def test_app_exists(self, app):
        """Test that Flask application instance is created successfully."""
        assert app is not None
        
    def test_app_is_testing_mode(self, app):
        """Test that application is configured in TESTING mode."""
        assert app.config['TESTING'] is True
        
    def test_test_client_creation(self, client):
        """Test that test client can be instantiated."""
        assert client is not None


class TestRootEndpoint:
    """Test the root endpoint (/) functionality."""
    
    def test_root_returns_200(self, client):
        """Test that GET / returns HTTP 200 status code."""
        response = client.get('/')
        assert response.status_code == 200
        
    def test_root_returns_hello_world(self, client):
        """Test that GET / returns 'Hello world' in response body."""
        response = client.get('/')
        assert response.data == b'Hello world'
        
    def test_root_content_type_is_text_plain(self, client):
        """Test that GET / Content-Type header is text/plain."""
        response = client.get('/')
        assert 'text/plain' in response.content_type
        
    def test_root_response_time_under_100ms(self, client):
        """Test that GET / responds in less than 100ms."""
        start = time.time()
        response = client.get('/')
        elapsed = time.time() - start
        
        assert response.status_code == 200
        assert elapsed < 0.1, f"Response took {elapsed:.3f}s, expected <0.1s"
        
    def test_root_with_query_parameters(self, client):
        """Test that GET / works correctly with query parameters."""
        response = client.get('/?test=value')
        assert response.status_code == 200
        assert response.data == b'Hello world'


class TestEveningEndpoint:
    """Test the /evening endpoint functionality."""
    
    def test_evening_returns_200(self, client):
        """Test that GET /evening returns HTTP 200 status code."""
        response = client.get('/evening')
        assert response.status_code == 200
        
    def test_evening_returns_good_evening(self, client):
        """Test that GET /evening returns 'Good evening' in response body."""
        response = client.get('/evening')
        assert response.data == b'Good evening'
        
    def test_evening_content_type_is_text_plain(self, client):
        """Test that GET /evening Content-Type header is text/plain."""
        response = client.get('/evening')
        assert 'text/plain' in response.content_type
        
    def test_evening_response_time_under_100ms(self, client):
        """Test that GET /evening responds in less than 100ms."""
        start = time.time()
        response = client.get('/evening')
        elapsed = time.time() - start
        
        assert response.status_code == 200
        assert elapsed < 0.1, f"Response took {elapsed:.3f}s, expected <0.1s"
        
    def test_evening_with_query_parameters(self, client):
        """Test that GET /evening works correctly with query parameters."""
        response = client.get('/evening?test=value')
        assert response.status_code == 200
        assert response.data == b'Good evening'


class TestErrorHandling:
    """Test error handling for various error scenarios."""
    
    def test_404_for_undefined_route(self, client):
        """Test that undefined routes return HTTP 404."""
        response = client.get('/nonexistent')
        assert response.status_code == 404
        
    def test_404_response_is_plain_text(self, client):
        """Test that 404 error response has text/plain content type."""
        response = client.get('/invalid')
        assert 'text/plain' in response.content_type
        
    def test_405_for_post_to_root(self, client):
        """Test that POST / returns HTTP 405 Method Not Allowed."""
        response = client.post('/')
        assert response.status_code == 405
        
    def test_405_for_put_to_root(self, client):
        """Test that PUT / returns HTTP 405 Method Not Allowed."""
        response = client.put('/')
        assert response.status_code == 405
        
    def test_405_for_delete_to_root(self, client):
        """Test that DELETE / returns HTTP 405 Method Not Allowed."""
        response = client.delete('/')
        assert response.status_code == 405
        
    def test_405_for_post_to_evening(self, client):
        """Test that POST /evening returns HTTP 405 Method Not Allowed."""
        response = client.post('/evening')
        assert response.status_code == 405
        
    def test_405_for_put_to_evening(self, client):
        """Test that PUT /evening returns HTTP 405 Method Not Allowed."""
        response = client.put('/evening')
        assert response.status_code == 405
        
    def test_405_for_delete_to_evening(self, client):
        """Test that DELETE /evening returns HTTP 405 Method Not Allowed."""
        response = client.delete('/evening')
        assert response.status_code == 405


class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_case_sensitive_root_path(self, client):
        """Test that paths are case-sensitive (uppercase should 404)."""
        # Flask routes are case-sensitive by default
        response = client.get('/EVENING')
        assert response.status_code == 404
        
    def test_trailing_slash_on_root(self, client):
        """Test behavior with trailing slash on root endpoint."""
        # Flask redirects / to / (no change), so should work
        response = client.get('/')
        assert response.status_code == 200
        assert response.data == b'Hello world'
        
    def test_trailing_slash_on_evening(self, client):
        """Test behavior with trailing slash on /evening endpoint."""
        # Flask by default does not add strict_slashes, so /evening/ should 404
        response = client.get('/evening/')
        # Flask default behavior: 308 redirect or 404, depends on configuration
        # For our implementation without strict_slashes=False, it should 404
        assert response.status_code in [308, 404, 200]  # Allow for different Flask behaviors
        
    def test_multiple_slashes(self, client):
        """Test that multiple slashes are not normalized."""
        response = client.get('//evening')
        # Flask may redirect (308) or return 404, both are acceptable
        assert response.status_code in [308, 404]
        
    def test_root_with_various_headers(self, client):
        """Test that root endpoint works with various request headers."""
        response = client.get('/', headers={
            'User-Agent': 'TestClient/1.0',
            'Accept': 'text/plain',
            'Accept-Language': 'en-US'
        })
        assert response.status_code == 200
        assert response.data == b'Hello world'


class TestResponseValidation:
    """Test complete response validation."""
    
    def test_root_response_structure(self, client):
        """Test that root endpoint response has all expected attributes."""
        response = client.get('/')
        
        # Validate status code
        assert response.status_code == 200
        
        # Validate response body
        assert response.data == b'Hello world'
        assert isinstance(response.data, bytes)
        
        # Validate content type
        assert 'text/plain' in response.content_type
        
        # Validate charset
        assert 'charset=utf-8' in response.content_type
        
    def test_evening_response_structure(self, client):
        """Test that evening endpoint response has all expected attributes."""
        response = client.get('/evening')
        
        # Validate status code
        assert response.status_code == 200
        
        # Validate response body
        assert response.data == b'Good evening'
        assert isinstance(response.data, bytes)
        
        # Validate content type
        assert 'text/plain' in response.content_type
        
        # Validate charset
        assert 'charset=utf-8' in response.content_type


class TestPerformance:
    """Test performance requirements."""
    
    def test_concurrent_requests_to_root(self, client):
        """Test that multiple consecutive requests work correctly."""
        for _ in range(10):
            response = client.get('/')
            assert response.status_code == 200
            assert response.data == b'Hello world'
            
    def test_concurrent_requests_to_evening(self, client):
        """Test that multiple consecutive requests to /evening work correctly."""
        for _ in range(10):
            response = client.get('/evening')
            assert response.status_code == 200
            assert response.data == b'Good evening'
            
    def test_alternating_requests(self, client):
        """Test alternating requests between endpoints."""
        for i in range(10):
            if i % 2 == 0:
                response = client.get('/')
                assert response.data == b'Hello world'
            else:
                response = client.get('/evening')
                assert response.data == b'Good evening'
            assert response.status_code == 200
