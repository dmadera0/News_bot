import requests
# Import the 'requests' library to make HTTP requests to external APIs

from flask import Flask, render_template, request, jsonify
# Import necessary modules from the Flask web framework

app = Flask(__name__)
# Initialize the Flask application

API_KEY = '3965fa071bd045479746bc619c056e5d'
# Define your API key for the NewsAPI service

# Define a function that fetches news articles from NewsAPI based on a search query
def get_news(query):
    # Construct the API URL with the search query and API key
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'
    # Send a GET request to the NewsAPI endpoint
    response = requests.get(url)
    # Return the JSON response containing news data
    return response.json()

# Define the route for the home page
@app.route('/')
def home():
    # Render the 'index.html' template when the user visits the home page
    return render_template('index.html')

# Define a route to fetch news data via a GET request
@app.route('/news', methods=['GET'])
def news():
    # Get the 'topic' parameter from the URL query string, default to 'technology' if not provided
    topic = request.args.get('topic', 'technology')
    # Fetch news articles related to the topic
    news_data = get_news(topic)
    # Return the news data as a JSON response
    return jsonify(news_data)

# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    # Enable debug mode for development (shows error messages and auto-reloads the server)
    app.run(debug=True)

