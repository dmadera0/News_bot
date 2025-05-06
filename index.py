import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import os

API_KEY = os.getenv('NEWS_API_KEY', '3965fa071bd045479746bc619c056e5d')
if not API_KEY:
    raise ValueError("No API key found. Please set the 'NEWS_API_KEY' environment variable.")

def get_news(query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'
    response = requests.get(url)
    return response.json()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/news', methods=['GET'])
def news():
    topic = request.args.get('topic', 'technology')
    news_data = get_news(topic)
    return jsonify(news_data)

if __name__ == '__main__':
    app.run(debug=True)
