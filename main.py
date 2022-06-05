from request_to_API import get_request
from parse_data import parse_data
from print_final_data import print_data
from exceptions import ApiServiceError
from pyfiglet import Figlet


def main() -> None:
    preview = Figlet(font='slant')
    print(preview.renderText('DICTIONARY'))
    word = input('Enter any word: ').strip().lower().split(' ')[0]
    try:
        response = get_request(word)
    except ApiServiceError:
        print("Can't find this word's definitions")
        exit(1)
    parsed_data = parse_data(word, response)
    print_data(parsed_data)

if __name__=='__main__':
    main()

