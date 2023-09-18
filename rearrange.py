import sys
import random

def rearrange_words():
    rearranged_string = ""
    arg_list = sys.argv.copy()
    arg_list.pop(0)
    random.shuffle(arg_list)
    print(*arg_list, sep = " ")
    return rearranged_string

if __name__ == "__main__":
    print(rearrange_words())