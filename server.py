from flask import Flask, jsonify, request
from flask_cors import CORS

# Create an instance of the Flask class
app = Flask(__name__)
CORS(app)
# Define a route and a view function
@app.route('/', methods=['POST'])
def hello_world():
    data = request.json
    print(data)
    return jsonify({'message': 'Data received without error'})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

