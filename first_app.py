"""Main script, uses other modules to generate sentences."""
from flask import Flask, request
from histogram import read_source
from histogram import histogram
from sample import choices_sentence
import sys

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

# source_text = sys.argv[1]
word_list = read_source(f'./data/volcanoes.txt')
histogram_output = histogram(word_list)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    # num = int(request.args.get('num'))
    sentence = choices_sentence(histogram_output, 15)
    return f"<p>{sentence}</p>"

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
