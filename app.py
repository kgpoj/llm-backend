from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def respond_to_query():
    if request.method == 'POST':
        data = request.get_json()
        query = data['query']
        response = 'Respond to ' + query
    else:
        response = 'Hello, new world!'

    return jsonify(response=response)

if __name__ == '__main__':
    app.run(port=3002)
