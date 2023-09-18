from histogram import histogram
from histogram import read_source
from histogram import listogram2 as listogram
import sys
import re
import timeit
import random

# source_text = sys.argv[1]

def output_formatter(histogram, num_to_output):
    '''
    returns num_to_output key:value pairs from a histogram in a more readable format.
    inputs: histogram - histogram as a dict
            num_to_output - int
    '''
    keys = list(histogram.keys())
    values = list(histogram.values())
    for _ in range (num_to_output):
        print(f'{keys[_]} => {values[_]}')

def percentage_output_formatter(histogram, num_to_output):
    '''
    returns num_to_output key:value pairs from a histogram in a more readable format, and as a percentage.
    inputs: histogram - histogram as a dict
            num_to_output - int
    '''
    keys = list(histogram.keys())
    values = list(histogram.values())
    total_sample_num = sum(values)
    for _ in range (num_to_output):
        print(f'{keys[_]} => {(values[_]/total_sample_num*100):.3}%')

def normalized_output_formatter(histogram, num_to_output):

    '''
    returns num_to_output key:value pairs from a histogram in a more readable format, normalized as probability.
    inputs: histogram - histogram as a dict
            num_to_output - int
    '''
    keys = list(histogram.keys())
    values = list(histogram.values())
    total_sample_num = sum(values)
    for _ in range (num_to_output):
        print(f'{keys[_]} => {(values[_]/total_sample_num):.4}')

# returns a random word from a list of unique words, aka uniform distribution
def random_histogram_word(histogram):
    '''
    returns a random word from a list of unique words generated from a histogram - functions as uniform distribution of words
    inputs: histogram - a histogram as a dict
    '''
    keys = list(histogram.keys())
    return keys[random.randint(0,len(keys)-1)]

def weighted_words_1(word_list):
    '''
    returns a random word from a list of unique words generated from a histogram - functions as uniform distribution of words
    inputs: histogram - a histogram as a dict
    '''
    return word_list[random.randint(0,len(word_list)-1)]

def weighted_words_2(histogram):
    '''
    returns a random word from a list of unique words generated from a histogram - functions as uniform distribution of words
    inputs: histogram - a histogram as a dict
    '''
    keys = list(histogram.keys())
    values = list(histogram.values())
    rebuilt_list = []
    for word in keys:
        for _ in range(values[keys.index(word)]):
            rebuilt_list.append(word)
    return rebuilt_list[random.randint(0,len(rebuilt_list)-1)]

def selection_histogram_1(word_list):
    '''
    returns a random word from a list of unique words generated from a histogram - functions as uniform distribution of words
    inputs: word_list - a list of words
    '''
    random_words = []
    for _ in range(10001):
        random_words.append(weighted_words_1(word_list))
    return histogram(random_words)

def choices_histogram(histogram_input, num_to_select):
    '''
    returns a histogram formed from weighted selection from a histogram of words using random.choices
    inputs: histogram_input - a histogram as a dict
    num_to_select - number of words to set k =
    '''
    random_words = []
    keys = list(histogram_input.keys())
    values = list(histogram_input.values())
    random_words = random.choices(keys, weights = values, k = num_to_select)
    return histogram(random_words)

def choices_sentence(histogram_input, num_to_select):
    '''
    returns a sentence formed from weighted selection from a histogram of words using random.choices
    inputs: histogram_input - a histogram as a dict
            num_to_select - number of words to set k =
    '''
    random_words = []
    keys = list(histogram_input.keys())
    values = list(histogram_input.values())
    random_words = random.choices(keys, weights = values, k = num_to_select)
    return f'{" ".join(random_words)}.'    

def selection_histogram_3(histogram):
    random_words = []
    for _ in range(10001):
        random_words.append(weighted_words_2(histogram))
    return histogram(random_words)

if __name__ == "__main__":
    test_text = 'one fish, two fish, red fish, blue fish'
    test_list = re.split(r'[^\w]+', test_text)
    # print(test_list)
    word_list = read_source(source_text)
    histogram_output = histogram(word_list)
    # output_formatter(histogram_output, 10)
    # percentage_output_formatter(histogram_output, 10)
    # normalized_output_formatter(histogram_output, 10)
    # print(histogram_output)
    # print(random_histogram_word(histogram_output))
    # print(weighted_words_1(word_list))
    # print(weighted_words_2(histogram_output))

    # print(selection_histogram_1(test_list))
    # print(selection_histogram_1(word_list)['the'])
    print(choices_histogram(histogram_output, 10))
    print(choices_sentence(histogram_output, 20))
    # print(histogram_output)
