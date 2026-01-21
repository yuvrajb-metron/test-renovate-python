#!/usr/bin/env python3
"""
Simple Python application to test Renovate dependency updates.

This is a minimal Flask app that uses several dependencies.
Renovate should detect outdated packages in requirements.txt
and create pull requests to update them.
"""

from flask import Flask, jsonify
import requests
import pandas as pd
import numpy as np
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def hello():
    """Simple hello endpoint."""
    return jsonify({
        'message': 'Hello from test app!',
        'timestamp': datetime.now(pytz.UTC).isoformat(),
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'pandas_version': pd.__version__,
        'numpy_version': np.__version__
    })

@app.route('/test-requests')
def test_requests():
    """Test the requests library by making a simple HTTP call."""
    try:
        response = requests.get('https://api.github.com', timeout=5)
        return jsonify({
            'status': 'success',
            'github_api_status': response.status_code
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
