import re


def text_to_list(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        read_list: list[str] = file.readlines()
        for idx, line in enumerate(read_list):
            if line == '\n':
                del read_list[idx]
            read_list[idx] = read_list[idx].strip()
    return read_list


if __name__ == '__main__':
    tests: list[str] = text_to_list('data/what category/data.txt')
    strings: list[str] = text_to_list('data/what category/strings.txt')

    output: str = ''
    for tindex, test in enumerate(tests):
        output = f'test{tindex}: "{test}"'
        for pindex, pattern in enumerate(strings):
            result = re.search(pattern,test)
            if result:
                output = f'{output}, matched with pattern{pindex}'
        print(output)
