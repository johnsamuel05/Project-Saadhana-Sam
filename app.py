from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')

@app.route('/')
def home():
    app.logger.info('Home endpoint accessed')
    return jsonify(message="Welcome to the Flask Web Application on GCP!")

@app.route('/config')
def config():
    app.logger.info('Configuration endpoint accessed')
    return jsonify(config="Current configuration details")

@app.route('/error')
def error():
    app.logger.error('Error endpoint accessed')
    return jsonify(error="This is a test error"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
