import random

def second_order_markov_chain(words):
    markov_chain = {}

    for i in range(len(words)-2):
        word_pair = (words[i], words[i+1])
        next_word = words[i+2]
        if word_pair in markov_chain:
            markov_chain[word_pair].append(next_word)
        else:
            markov_chain[word_pair] = [next_word]
    print(chain)
    return markov_chain

def third_order_markov_chain(words):
    markov_chain = {}

    for i in range(len(words)-3):
        word_pair = (words[i], words[i+1], words[i+2])
        next_word = words[i+3]
        if word_pair in markov_chain:
            markov_chain[word_pair].append(next_word)
        else:
            markov_chain[word_pair] = [next_word]
    return markov_chain

def fourth_order_markov_chain(words):
    markov_chain = {}

    for i in range(len(words)-4):
        word_pair = (words[i], words[i+1], words[i+2], words[i+3])
        next_word = words[i+4]
        if word_pair in markov_chain:
            markov_chain[word_pair].append(next_word)
        else:
            markov_chain[word_pair] = [next_word]
    print(chain)
    return markov_chain

# class Ngram(dict):
#     """Ngram creates an nth-order Markov chain from a corpus"""
#     def __init__(self, word_list = None, order = 2):
#         """Takes a word list and order of ngram"""
#         super(Ngram, self).__init__()
#         if word_list is not None:
#             markov_chain = {}
#             word_sequence = []
#             for i in range(len(words) - order):
#                 word_group = tuple(words[i:i+order])
#                 next_word = words[i + order]
#                 if word_group in markov_chain:
#                     self[word_group].append(next_word)
#                 else:
#                     self[word_group] = [next_word]

#     def add_count(self, index, word_list, count = 1):
#         """Generates a markov histogram from a provided word list"""
#         word = word_list[index]
#         if word in self:
#             self[word].append(word_list[index + 1])
#         else:
#             self.update({word_list[index]: [word_list[index + 1]]})

#     def random_markov_sentence(self, max_num):
#         """Generates a random sentence from a markov chain"""
#         chosen_words = [random.choice(self["START"])]
#         for _ in range(max_num - 1):
#             word = random.choice(self[chosen_words[-1]])
#             if word == "END":
#                 break
#             chosen_words.append(word)
#         sentence = " ".join(chosen_words) + random.choice(".....!?")
#         sentence = sentence[0].capitalize() + sentence[1:]
#         return sentence


def ngram(words, order = 2):
    """Takes a word list and generates an ngram with default order of 2 if argument not provided"""
    markov_chain = {}
    word_sequence = []

    for i in range(len(words) - order):
        word_group = tuple(words[i:i+order])
        next_word = words[i + order]
        if word_group in markov_chain:
            markov_chain[word_group].append(next_word)
        else:
            markov_chain[word_group] = [next_word]
    return markov_chain

def sentence_ngram(words, order = 2):
    markov_chain = {}
    word_sequence = []
    starting_tuples = []

    for i in range(len(words) - order):
        word_group = tuple(words[i:i+order])
        if word_group[-1][-1] in ['.','!','?']:
            starting_tuples.append(tuple(words[i+order:i+(2*order)]))
        next_word = words[i + order]
        if word_group in markov_chain:
            markov_chain[word_group].append(next_word)
        else:
            markov_chain[word_group] = [next_word]
    return starting_tuples, markov_chain

# def sentence_ngram(text, order = 2):
#     words = text.split()
#     markov_chain = {}
#     word_sequence = []
#     starting_tuples = []

#     for i in range(len(words) - order):
#         word_group = tuple(words[i:i+order])
#         if word_group[-1][-1] in ['.','!','?']:
#             words[i]
#         next_word = words[i + order]
#         if word_group in markov_chain:
#             markov_chain[word_group].append(next_word)
#         else:
#             markov_chain[word_group] = [next_word]
#     return markov_chain

def generate_markov_sentence(markov_chain, length, order = 2):
    word_group = random.choice(list(markov_chain.keys()))
    chosen_words = list(word_group)

    for i in range(length - order):
        next_word = random.choice(markov_chain[word_group])
        chosen_words.append(next_word)
        word_group = word_group[1:order]
        word_group = list(word_group)
        word_group.append(next_word)
        word_group = tuple(word_group)
    sentence = " ".join(chosen_words) + random.choice(".....!?")
    return sentence

def generate_sentence_2(markov_chain, starters, order = 2):
    """generates a sentence from an ngram.  Takes a full ngram, a list of starter tuples, 
    a sentence length and the order of the ngram"""
    word_group = random.choice(starters)
    chosen_words = list(word_group)

    # for i in range(length - order):
    while chosen_words[-1][-1] not in ['.','!','?']:
        next_word = random.choice(markov_chain[word_group])
        chosen_words.append(next_word)
        word_group = word_group[1:order]
        word_group = list(word_group)
        word_group.append(next_word)
        word_group = tuple(word_group)
    return ' '.join(chosen_words)
