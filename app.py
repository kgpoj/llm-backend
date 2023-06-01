from flask import Flask, request, jsonify
from flask_cors import CORS

from jarvis import Jarvis

app = Flask(__name__)
CORS(app)
jarvis = Jarvis()

@app.route('/', methods=['GET', 'POST'])
def respond_to_query():
    if request.method == 'POST':
        request_data = request.get_json()
        data = request_data['data']
        question = request_data['question']
        history = request_data['history']
        response = jarvis.respond_to_question(question, data, history)
    else:
        response = 'Hello, world'

    return jsonify(response=response)
