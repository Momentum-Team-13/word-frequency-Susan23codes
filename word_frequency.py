import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    text = open_and_read_file(file)
    filtered_words = clean_and_filter_text(text)
    word_frequency_object = build_word_frequency_object(filtered_words)
    printing_final_count(word_frequency_object)


def open_and_read_file(file):
    with open(file) as open_file:
        text = open_file.read()
    return text


def clean_and_filter_text(text):
    lowered_text = text.lower().replace("—", " ").replace("-", " ").replace('“', ' ').replace('”', ' ')
    unpunctuated_text = lowered_text.translate(
        str.maketrans('', '', string.punctuation.replace("'", "")))
    word_array = unpunctuated_text.split()
    filtered_words = [word for word in word_array if word not in STOP_WORDS]
    return filtered_words

def build_word_frequency_object(filtered_words):
    word_frequency_object = {}
    for word in filtered_words:
        if word in word_frequency_object:
            word_frequency_object[word] = word_frequency_object[word] + 1
        else:
            word_frequency_object.update({word: 1})
    return word_frequency_object


def printing_final_count(word_frequency_object):
    print(word_frequency_object)
    word_frequency_object_key = {k: v for k, v in sorted(
        word_frequency_object.items(), key=lambda item: item[0]
    )}
    # print("************")
    # print(word_frequency_object)
    # print(word_frequency_object_key)
    word_frequency_object_value = {k: v for k, v in sorted(
        word_frequency_object_key.items(), key=lambda item: item[1], reverse=True
    )}
    # print("************")
    # print(word_frequency_object)
    # print(word_frequency_object_key)
    # print(word_frequency_object_value)
    for key, value in word_frequency_object_value.items():
        print(f'{key.rjust(20)} | {value} {value * "*"}')

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)