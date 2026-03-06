import os
import uuid
import time
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

# Disable caching for all responses
@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route('/', methods=['GET'])
def home():
    """Root endpoint - returns basic server info with unique identifiers"""
    return jsonify({
        'message': 'Testing Hub Server',
        'status': 'active',
        'timestamp': datetime.now().isoformat(),
        'unique_id': str(uuid.uuid4()),
        'elapsed_seconds': time.time()
    })


@app.route('/test', methods=['GET', 'POST'])
def test_endpoint():
    """Test endpoint - echoes request and adds unique identifiers"""
    return jsonify({
        'method': request.method,
        'path': request.path,
        'args': dict(request.args),
        'timestamp': datetime.now().isoformat(),
        'request_id': str(uuid.uuid4()),
        'server_pid': os.getpid()
    })


@app.route('/echo', methods=['POST'])
def echo():
    """Echo endpoint - returns posted data with cache-busting info"""
    data = request.get_json() if request.is_json else request.form.to_dict()
    return jsonify({
        'received': data,
        'echo_id': str(uuid.uuid4()),
        'timestamp': datetime.now().isoformat()
    })


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'check_id': str(uuid.uuid4())
    })


if __name__ == '__main__':
    print("Starting Testing Hub Server...")
    print("Server running on http://localhost:5000")
    print("Endpoints:")
    print("  GET  http://localhost:5000/          - Root endpoint")
    print("  GET/POST http://localhost:5000/test  - Test endpoint")
    print("  POST http://localhost:5000/echo      - Echo endpoint")
    print("  GET  http://localhost:5000/health    - Health check")
    print("\nNote: All responses include unique IDs and timestamps to prevent caching")
    app.run(debug=True, host='0.0.0.0', port=5000)
