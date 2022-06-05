import requests
from exceptions import ApiServiceError

def get_request(word: str) -> list:
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url)
    if response.status_code != 200:
        raise ApiServiceError
    return response.json()
    
    

