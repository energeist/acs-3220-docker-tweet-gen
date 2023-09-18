import timeit
import sys
import random
# import mmap
from decorators import runtime_calc

num_words = int(sys.argv[1])
autocomplete_string = ""

if len(sys.argv) > 2:
    autocomplete_string = str(sys.argv[2])

words = []

def read_dictionary():
    start = timeit.default_timer()
    with open("/usr/share/dict/words") as text:
        words = text.read().split()
    end = timeit.default_timer()
    print(f'Time to read words: {(end - start):.6f} seconds')  
    return words

# def read_dictionary():
#     start = timeit.default_timer()
#     with open("/usr/share/dict/words", 'rb') as f:
#         mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
#         words = mmapped_file.read().decode().split('\n')
#     end = timeit.default_timer()
#     print(f'Time to read words: {end - start} seconds')  
#     return words

@runtime_calc
def random_sentence():
    # words = read_dictionary()
    sentence = ""
    chosen_words = []
    for _ in range(num_words):
        random_word = random.choice(words)
        chosen_words.append(random_word)    
    return print(f'{" ".join(chosen_words)}.')

@runtime_calc
def random_sentence_2():
    # words = read_dictionary()
    sentence = ""
    index_list = []
    chosen_words = []

    for _ in range(num_words):
        index_list.append(random.randint(0,len(words)-1))
    # index_list.sort()

    for index in index_list:
        chosen_words.append(words[index])
    return print(f'{" ".join(chosen_words)}.')

potential_words = []
start_with_string_words = []

@runtime_calc
def random_sentence_3():
    # words = read_dictionary()
    random_words = random.sample(words, k=num_words)
    return print(f"{' '.join(random_words)}.")

@runtime_calc
def random_sentence_4():
    word_list = []
    index_list = []

    for _ in range(int(sys.argv[1])):
        index_list.append(random.randint(0,102401))
    infile = open("/usr/share/dict/words","r")

    for index in index_list:
        word_list.append(infile.readline(index))
    infile.close()

def auto_complete():
    with open("/usr/share/dict/words") as text:
        words = text.readlines()
    print(len(words))
    for word in words:
        if autocomplete_string.lower() in word.strip("\n").lower():
            potential_words.append(word.strip("\n"))
        if autocomplete_string.lower() == word.strip("\n").lower()[:len(autocomplete_string)]:
            start_with_string_words.append(word)
        
    if len(potential_words) == 0:
        return print("There are no words that match that string")
    else:
        return print(f"There are {len(potential_words)} words that contain the substring '{autocomplete_string}'. Of those words, {len(start_with_string_words)} of them begin with '{autocomplete_string}'. The list begins with {potential_words[0]} and ends with {potential_words[-1]}.")


if __name__ == "__main__":
    words = read_dictionary()
    random_sentence()
    random_sentence_2()
    random_sentence_3()
    random_sentence_4()
    potential_words = []
    if autocomplete_string:
        auto_complete()
