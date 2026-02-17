import os
import logging
import datetime
import socket
from flask import Flask, jsonify

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration from environment
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
APP_COMMIT_SHA = os.getenv('APP_COMMIT_SHA', 'unknown')
PORT = int(os.getenv('PORT', 8080))
HOSTNAME = socket.gethostname()

@app.route('/api/v1/info')
def info():
    """Return app info and metadata"""
    logger.info('GET /api/v1/info')
    return jsonify({
        'time': datetime.datetime.now().isoformat(),
        'hostname': HOSTNAME,
        'version': APP_VERSION,
        'commit': APP_COMMIT_SHA,
        'message': 'You are doing great, human!!! XOXO',
    }), 200

@app.route('/')
def root():
    """Root endpoint - basic health check"""
    logger.info('GET /')
    return jsonify({
        'status': 'ok',
        'service': 'python-probe',
        'version': APP_VERSION
    }), 200

@app.route('/health')
def health():
    """Health check endpoint"""
    logger.info('GET /health')
    return jsonify({'status': 'up'}), 200

@app.route('/healthz')
def healthz():
    """Kubernetes-style health check"""
    logger.info('GET /healthz')
    return '', 200

@app.route('/ready')
def ready():
    """Readiness probe endpoint"""
    logger.info('GET /ready')
    return '', 200

@app.route('/live')
def live():
    """Liveness probe endpoint"""
    logger.info('GET /live')
    return '', 200

@app.route('/api/v1/version')
def version():
    """Return version information"""
    logger.info('GET /api/v1/version')
    return jsonify({
        'version': APP_VERSION,
        'commit': APP_COMMIT_SHA
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    logger.warning(f'404 - Path not found: {error}')
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f'500 - Internal Server Error: {error}')
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    logger.info(f'Starting python-probe v{APP_VERSION} on {HOSTNAME}')
    app.run(host='0.0.0.0', port=PORT, debug=False)

