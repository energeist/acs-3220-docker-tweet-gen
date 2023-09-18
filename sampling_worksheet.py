import random

histogram = [('cats', 3), ('dogs', 4), ('rabbits', 2), ('turtles', 1)]

def sample(histogram):
    """Return a word from this histogram, randomly sampled by weighting each word's probability of being chosen by its observed frequency.""" 
    tokens = sum([count for word, count in histogram])
    # Count total tokens
    dart = random.randint(1, tokens)
    dart = 8	
    # Throw a dart on the number line 
    # Note: Assume that randint returns 8 here and dart stores the value 8 
    fence = 0
    # Border of where each word splits the number line 
    for word, count in histogram:	
    # Loop over each word and its count 
        fence += count	
        print(f'word: {word}, count: {count}, fence: {fence}')
        # Move this word's fence border to the right 
        if fence >= dart: 
            # Check if this word's fence is past the dart 
            return word	
            # Fence is past the dart, so choose this word

print(sample(histogram))