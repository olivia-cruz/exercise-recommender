from flask import Flask, jsonify
from flask_cors import CORS

from constants import EXERCISES


app = Flask(__name__)

CORS(app)

PORT = 5001

@app.route('/exercises', methods=['GET'])
def get_exercises():
    response = jsonify(EXERCISES)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
