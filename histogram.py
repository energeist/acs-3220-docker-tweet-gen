import sys
import timeit
import re

test_text = 'one fish, two fish, red fish, blue fish'

# source_text = sys.argv[1]

def read_source(source_text):
    """reads a source text and splits into a list of words, removing special characters"""
    with open(f"./{source_text}") as text:
        word_list = re.split(r'[^\w]+',text.read())
    return word_list

# add items by key and increment
def histogram(word_list):
    """creates a histogram as a dictionary from a list of words"""
    histogram = {}
    for word in word_list:
        word = word.lower()
        if word in histogram:
            histogram[word.lower()] += 1
        else:
            histogram[word.lower()] = 1
    # return histogram
    return dict(sorted(histogram.items(), key=lambda x: x[1], reverse=True))

# add items by count of list (slow)
def histogram2(word_list):
    """creates a histogram as a dictionary from a list of words"""
    histogram = {}
    for word in word_list:
        word = word.lower()
        histogram[word] = word_list.count(word)
    return histogram
    # return dict(sorted(histogram.items(), key=lambda x: x[1], reverse=True))

#Dani's version
def dictogram(word_list):
    """creates a histogram as a dictionary from a list of words"""
    dictogram = {}
    for word in word_list:
        word_count = dictogram.get(word, 0) + 1
        dictogram[word] = word_count
    return dictogram

def listogram(word_list):
    """creates a histogram as a list of lists from a list of words"""
    listogram = []
    words = []
    count = []
    for word in word_list:
        for index in range(len(listogram)):
            if index[0] == word:
                index[1] += 1
            if index == len(listogram) - 1:
                listogram.append[word, 1]
    return listogram

def listogram2(word_list):
    """creates a histogram as a list of lists from a list of words"""
    listogram = []
    unique_words = []
    count = []
    for word in word_list:
        if unique_words.count(word.lower()) == 0:
            unique_words.append(word.lower())
            count.append(1)
        else:
            count[unique_words.index(word.lower())] += 1
    for item in unique_words:
        listogram.append([item, count[unique_words.index(item)]])
    return listogram

def listogram3(word_list):
    """creates a histogram as a list of tuples from a list of words"""
    listogram = []
    unique_words = []
    count = []
    for word in word_list:
        if unique_words.count(word.lower()) == 0:
            unique_words.append(word.lower())
            count.append(1)
        else:
            count[unique_words.index(word.lower())] += 1
    listogram = list(zip(unique_words, count))
    return listogram

def invert(histogram_to_invert):
    """creates an inverted histogram with counts as the key and a list of words 
        with the corresponding counts as the value"""
    inverted_histogram = {}
    for key in histogram_to_invert.keys():
        if histogram_to_invert[key] in inverted_histogram:
            inverted_histogram[histogram_to_invert[key]].append(key)
        else:
            inverted_histogram[histogram_to_invert[key]] = [key]
    return(inverted_histogram) 

def unique_words(histogram):
    """returns the number of unique words (types) in a histogram"""
    return len(histogram.keys())

def frequency(word, histogram):
    """returns the count of the provided word"""
    return histogram[word]

if __name__ == "__main__":
    print("reading text:")
    start = timeit.default_timer()
    word_list = read_source(source_text)
    end = timeit.default_timer()
    print(f"Time to run {end - start} seconds\n")

    print("histogram 1:")
    start = timeit.default_timer()
    histogram(word_list)
    end = timeit.default_timer()
    print(f"Time to run {end - start} seconds\n")
    # print(unique_words(histogram(source_text)))
    # print(frequency(sys.argv[2], histogram2(source_text)))

    print("histogram 2:")
    start = timeit.default_timer()
    histogram2(word_list)
    end = timeit.default_timer()
    print(f"Time to run {end - start} seconds\n")
    # print(unique_words(histogram2(source_text)))
    # print(frequency(sys.argv[2], histogram2(source_text)))

    print("invert histogram 1:")
    start = timeit.default_timer()
    invert(histogram(word_list))
    end = timeit.default_timer()
    print(f"Time to run {end - start} seconds\n")

    print("dictogram:")
    start = timeit.default_timer()
    dictogram(word_list)
    end = timeit.default_timer()
    print(f"Time to run {end - start} seconds\n")

    print("listogram 2:")
    start = timeit.default_timer()
    listogram2(word_list)
    end = timeit.default_timer()
    print(f"Time to run {end - start} seconds\n")

    print("listogram 3:")
    start = timeit.default_timer()
    listogram3(word_list)
    end = timeit.default_timer()
    print(f"Time to run {end - start} seconds\n")


    print("testing things")
    testdict = {
        'key': 1,
        'dog': 2
    }

    testdict.get('key')
    testdict.get('cat')