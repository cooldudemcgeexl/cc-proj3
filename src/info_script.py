import os
from functools import reduce
from itertools import chain, islice
from socket import gethostbyname, gethostname

DATA_DIR = 'data'


def list_text_files():
    text_files = list(filter(lambda x: x.endswith('.txt') ,os.listdir()))
    print(f'Text files in {os.getcwd()}:')
    [print(text_file) for text_file in text_files]
    print('\n')

def count_words_in_file(filename: str):
    lines = get_line_array(filename)
    return reduce(lambda x,y: x + len(y.split(' ')),lines,0)

def get_line_array(filename: str):
    lines = []
    with open(file=filename, mode='r') as file:
        lines = file.readlines()
    lines = list(map(lambda x: x.strip(' \n!.;,').lower(), lines))
    lines = list(filter(lambda x: len(x), lines))
    return lines

def get_word_counts():
    if_wc = count_words_in_file('IF.txt')
    limerick_wc = count_words_in_file('Limerick.txt')

    print(f'Words in IF.txt: {if_wc}')
    print(f'Words in Limerick.txt: {limerick_wc}')
    print(f'Grand total of words: {if_wc+limerick_wc}')
    print('\n')

def word_freq_from_list(word_list: list[str]) -> dict[str,int]:
    word_set = set(word_list)
    word_freq_dict = {}
    for word in word_set:
        word_freq_dict[word] = word_list.count(word)
    
    sorted_word_freq = dict(sorted(word_freq_dict.items(),key=lambda item:item[1], reverse=True))
    return sorted_word_freq

def get_word_freq(filename: str):
    lines = get_line_array(filename=filename)
    words = list(map(lambda x: x.split(' '), lines))
    words_merged = list(chain(*words))
    word_freq_dict = word_freq_from_list(words_merged)

    word_freq_top3 = dict(islice(word_freq_dict.items(),3))
    print('Top 3 words in IF.txt:')
    for key, value in word_freq_top3.items():
        print(f'{key}: {value}')
    print('\n')

def get_ip_addr():
    print(f"This machine's IP address: {gethostbyname(gethostname())}")

if __name__ == "__main__":
    os.chdir(DATA_DIR)    
    list_text_files()
    get_word_counts()
    get_word_freq('IF.txt')
    get_ip_addr()

