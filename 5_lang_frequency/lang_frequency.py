import os
import re
import pprint as pp
from collections import defaultdict, Counter


def load_data(filepath):
    with open(filepath, "r") as data_file:
        data_file = data_file.read()
        return data_file


def make_letters_lower(data_file):
    return data_file.lower()


def get_split_text_without_punctuation(data_file):
    words = re.split("[ \n_;,'`.?!:'{}#<>=^()]", data_file)
    return words


def empty_words_removing(words):
    filtered_words = list(filter(None, words))
    return filtered_words


def get_most_frequent_words(filtered_words, number_of_most_common_words=10):
    most_freq_words = Counter(filtered_words).most_common(number_of_most_common_words)
    return most_freq_words


def main():
    filepath = input('Enter the path to .txt file: ')
    if os.path.exists(filepath):
        data_loading = load_data(filepath)
        words_with_lower_letters = make_letters_lower(data_loading)
        splitted_text_without_punctuation = get_split_text_without_punctuation(words_with_lower_letters)
        words_without_empty_staff = empty_words_removing(splitted_text_without_punctuation)
        most_frequent_words = get_most_frequent_words(words_without_empty_staff)
        print('\nThe most frequent words of .txt with the numbers of entrances:')
        pp.pprint(most_frequent_words)
    else:
        print('File is not found')


if __name__ == '__main__':
    main()
