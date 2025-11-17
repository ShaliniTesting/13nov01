"""
Flask web server application implementing the same functionality as the original Node.js Express server.

This application provides two GET endpoints:
- Root endpoint (/) returning 'Hello world' as plain text
- Evening endpoint (/evening) returning 'Good evening' as plain text

The server runs on port 5000 (Flask default) and includes error handlers for 404 and 405 responses.
"""

from flask import Flask, make_response, Response

# Initialize Flask application
app = Flask(__name__)


@app.route('/', methods=['GET'])
def root() -> Response:
    """
    Root endpoint handler.
    
    Returns:
        Response: Plain text response containing 'Hello world' with HTTP 200 status
    """
    response = make_response('Hello world', 200)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response


@app.route('/evening', methods=['GET'])
def evening() -> Response:
    """
    Evening endpoint handler.
    
    Returns:
        Response: Plain text response containing 'Good evening' with HTTP 200 status
    """
    response = make_response('Good evening', 200)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response


@app.errorhandler(404)
def not_found(error) -> Response:
    """
    Handle 404 Not Found errors.
    
    Args:
        error: The error object
        
    Returns:
        Response: Plain text error message with HTTP 404 status
    """
    response = make_response('404 Not Found', 404)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response


@app.errorhandler(405)
def method_not_allowed(error) -> Response:
    """
    Handle 405 Method Not Allowed errors.
    
    Args:
        error: The error object
        
    Returns:
        Response: Plain text error message with HTTP 405 status
    """
    response = make_response('405 Method Not Allowed', 405)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response


# Run the application
if __name__ == '__main__':
    print('Server is running on http://localhost:5000')
    app.run(host='localhost', port=5000, debug=True)
