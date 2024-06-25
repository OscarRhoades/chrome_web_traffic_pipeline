from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

from preprocess import append_to_csv

app = Flask(__name__)
CORS(app)  

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    log_type = data.get('type')
    message = data.get('message')
    timestamp = data.get('timestamp', datetime.datetime.now().isoformat())

    
    append_to_csv("action_data.csv",[timestamp, log_type.upper(), message])
    print(f"[{timestamp}] {log_type.upper()}: {message}")

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
