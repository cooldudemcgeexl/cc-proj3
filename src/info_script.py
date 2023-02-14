import os
from functools import reduce

DATA_DIR = 'data'


def list_text_files():
    text_files = list(filter(lambda x: x.endswith('.txt') ,os.listdir()))
    print(f'Text files in {os.getcwd()}:')
    [print(text_file) for text_file in text_files]
    print('\n')

def count_words_in_file(filename: str):
    lines = []
    with open(file=filename, mode='r') as file:
        lines = file.readlines()
    lines = list(map(lambda x: x.strip(), lines))
    lines = list(filter(lambda x: len(x), lines))
    return reduce(lambda x,y: x + len(y.split(' ')),lines,0)

def get_word_counts():
    if_wc = count_words_in_file('IF.txt')
    limerick_wc = count_words_in_file('Limerick.txt')

    print(f'Words in IF.txt: {if_wc}')
    print(f'Words in Limerick.txt: {limerick_wc}')
    print(f'Grand total of words: {if_wc+limerick_wc}')


if __name__ == "__main__":
    os.chdir(DATA_DIR)    
    list_text_files()
    get_word_counts()
    
