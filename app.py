"""Main script, uses other modules to generate sentences."""
from flask import Flask, request, render_template
from higher_order_markov import ngram, generate_markov_sentence, sentence_ngram, generate_sentence_2
from markov import read_source_2
from markov import markov
from sample import choices_sentence
import sys
import re

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

word_list = read_source_2(f'./data/marx.txt')
markov_chain = {}
# Initialize with 2nd order markov chain
order = 2
sentence_starters, full_ngram = sentence_ngram(word_list, order)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = ""
    generated_text = ''

    sentences_input = request.args.get('num_sentences') # can add ?num_sentences=<num_sentences> to URL for more sentences
    if sentences_input:
        num_sentences = int(sentences_input)
        for _ in range(num_sentences):
            sentence = generate_sentence_2(full_ngram, sentence_starters, order)
            generated_text += sentence + " "
    else:
        if not sentences_input: # generate appropriate length sentences for a tweet if only one sentence
            while len(generated_text) < 50 or len(generated_text) > 280:
                generated_text = generate_sentence_2(full_ngram, sentence_starters, order)
    return render_template('index.html', sentence=generated_text)

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
