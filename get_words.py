import random

def get_word(min_length):
    word_list_file = 'words_list.txt'
    words_list = []
    final_word = ""
    with open(word_list_file, 'r') as wordlist:
        for word in wordlist:
            word = word.strip().lower()
            if len(word) >= min_length:
                words_list.append(word)
    
    if words_list:
        final_word = random.choice(words_list)
    
    return final_word