import random
 
WORDLIST = 'wordlist.txt'
 
def get_random_word(min_word_length):
    num_words_processed = 0
    current_word = None
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                current_word = word
    return current_word