import re

keywords_list: list[str] = [
    'aa-overlay',
    'ads',
    'pace',
    'pb',
    'what-category',
    'wr',
    'view-count'
]


def text_to_list(file_path: str) -> list[str]:
    with open(file_path, mode='r') as file:
        read_list: list[str] = file.readlines()
        for idx, line in enumerate(read_list):
            if line == '\n':
                del read_list[idx]
            read_list[idx] = read_list[idx].strip()
    return read_list


def test_keyword(keyword_name: str):
    tests: list[str] = text_to_list(f'data/{keyword_name}/data.txt')
    patterns: list[str] = text_to_list(f'data/{keyword_name}/patterns.txt')

    for tindex, test in enumerate(tests):
        output: str = f'test{tindex}: \"{test}\"'
        for pindex, pattern in enumerate(patterns):
            result = re.search(pattern, test, flags=re.I)
            if result:
                output = f'{output}, matched with pattern{pindex}'
        print(output)


if __name__ == '__main__':
    for keyword in keywords_list:
        test_keyword(keyword)
