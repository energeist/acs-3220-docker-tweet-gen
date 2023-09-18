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

def read_source(source_text):
    with open(f"./{source_text}") as text:
        word_list = re.split(r'[^\w]+',text.read())
    return word_list