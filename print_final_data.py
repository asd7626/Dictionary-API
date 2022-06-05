from parse_data import Dictionary_NT


def print_data(data: Dictionary_NT) -> None:
    print('The Word:', data.word)
    print('All Definitions:')
    for index, word in zip([i for i in range(1, len(data.definitions) + 1)], data.definitions):
        print(index, '-' ,word)

