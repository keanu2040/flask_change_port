from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
