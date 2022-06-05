from typing import NamedTuple


class Dictionary_NT(NamedTuple):
    word: str
    definitions: list


def _parse_meanings_blocks(data1: list) -> list:
    blocks = [i['meanings'] for i in data1]
    return blocks[0]


def _parse_definitions_blocks(data2: list) -> list:
    result = []
    for part in data2:
        result.extend([value for key, value in part.items() if key == 'definitions'])
    return result


def _parse_all_definitions(data3: list) -> list:
    result = []
    for part in data3:
        for p in part:
            result.extend([value for key, value in p.items() if key == 'definition'])
    return result

def parse_data(word: str, data: list) -> Dictionary_NT:
    meanings_blocks = _parse_meanings_blocks(data)
    definitions_blocks = _parse_definitions_blocks(meanings_blocks)
    definitions = _parse_all_definitions(definitions_blocks)
    result_NT =  Dictionary_NT(word=word,  definitions=definitions)
    return result_NT    




