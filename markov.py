from __future__ import division, print_function  # Python 2 and 3 compatibility
import re
import random

class MarkovChain(dict):
    """MarkovChain creates a Markov chain from a corpus"""
    def __init__(self, word_list = None, dict = None):
        # self.types = 0
        # self.tokens = 0
        super(MarkovChain, self).__init__()
        if word_list is not None:
            for i in range(len(word_list)-1):
                self.add_count(i, word_list)
            self.pop("END")

    def add_count(self, index, word_list, count = 1):
        """Generates a markov histogram from a provided word list"""
        word = word_list[index]
        if word in self:
            self[word].append(word_list[index + 1])
        else:
            self.update({word_list[index]: [word_list[index + 1]]})

    def random_markov_sentence(self, max_num):
        """Generates a random sentence from a markov chain"""
        chosen_words = [random.choice(self["START"])]
        for _ in range(max_num - 1):
            word = random.choice(self[chosen_words[-1]])
            if word == "END":
                break
            chosen_words.append(word)
        sentence = " ".join(chosen_words) + random.choice(".....!?")
        sentence = sentence[0].capitalize() + sentence[1:]
        return sentence

def read_source(source_text):
    """Built for a first order markov chain implementation. Reads a source text and splits into a list of words, 
    removing special characters and adding entry and exit points."""
    with open(f"{source_text}") as text:
        text = text.read()
        text = re.sub(r'[.!?]+', " END START ", text)
        text = "START " + text
        word_list = re.sub(r'[^a-zA-Z\’\']+', " ", text).split()
    return word_list

def read_source_2(source_text):
    """reads a source text and splits into a list of words, removing special characters and adding entry and exit points."""
    with open(f"{source_text}") as text:
        text = text.read()
        text = re.sub(r'\s[\.\,]*[A-HJ-Za-z]?[\.\,]\s', " ", text)
        text = re.sub(r'\b(\w|\d)[^\w\s]', " ", text) # remove artifacts like e.
        text = re.sub(r'\b[A-Z]{2,}'," ",text) # remove all ALLCAPS words
        text = re.sub(r'\s\W*\s', " ", text) # remove random floating punctuation
        word_list = re.sub(r'[^a-zA-Z\,\’\'\.\!\?]+', " ", text).split()
    return word_list

def add_entry_and_exit(text):
    text = "START " + text
    text = re.sub(r'[,]+', "", text)
    text = re.sub(r'[.!?]+', " END START ", text).split()
    return text

sample_text = "One fish, two fish, red fish, blue fish. Fun fish, brew fish, sled fish, shoo fish? Bun fish, shoe fish, dread fish, new fish!"

source_text = './data/marx.txt'

markov = MarkovChain(read_source(source_text))
