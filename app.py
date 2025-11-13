from flask import Flask, render_template, jsonify, send_from_directory
import redis
import os
import socket

app = Flask(__name__, static_folder='static', template_folder='templates')

# Configurazione Redis
redis_host   = os.getenv('REDIS_HOST', 'localhost')
redis_port   = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/increment/<counter_name>')
def increment(counter_name):
    try:
        value = redis_client.incr(counter_name)
        return jsonify({'counter': counter_name, 'value': value})
    except Exception as e:
        return jsonify({'error':str(e)}), 500

@app.route('/get/<counter_name>')
def get_counter(counter_name):
    try:
        value = redis_client.get(counter_name) or 0
        return jsonify({'counter': counter_name, 'value': int(value)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reset/<counter_name>')
def reset(counter_name):
    try:
        redis_client.delete(counter_name)
        return jsonify({'message': f'Counter {counter_name} reset'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# health check endpoint
@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'host': socket.gethostname()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)