import re


def text_to_list(file_path: str) -> list[str]:
    with open(file_path, mode='r') as file:
        read_list: list[str] = file.readlines()
        for idx, line in enumerate(read_list):
            if line == '\n':
                del read_list[idx]
            read_list[idx] = read_list[idx].strip()
    return read_list


def test_keywords(keywords: list[str], highlight_fails: bool = False):
    fail_output: str = "\n\nthe following tests matched none of the patterns:"

    for keyword in keywords:
        tests: list[str] = text_to_list(f'data/{keyword}/data.txt')
        patterns: list[str] = text_to_list(f'data/{keyword}/patterns.txt')

        for tindex, test in enumerate(tests):
            output: str = f"{keyword}-test{tindex}: \"{test}\""
            for pindex, pattern in enumerate(patterns):
                if re.search(pattern, test, flags=re.I):
                    output = f"{output}, matched with pattern{pindex}"
            print(output)
            
            if highlight_fails:
                if output == f"{keyword}-test{tindex}: \"{test}\"":
                    fail_output += f"\n{output}"

    if highlight_fails:
        print(fail_output)


if __name__ == '__main__':
    keywords_list: list[str] = [
        'aa-overlay',
        'ads',
        'pace',
        'pb',
        'what-category',
        'wr',
        'view-count'
    ]

    test_keywords(keywords_list, highlight_fails=True)