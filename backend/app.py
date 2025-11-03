from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
  return jsonify({"message": "FitCol Backend is running!", "status": "success"})

@app.route('/health')
def health_check():
  return jsonify({"status": "healthy"})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)