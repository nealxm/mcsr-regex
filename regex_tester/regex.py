import re

from regex_tester.logger import log


def text_to_list(file_path: str) -> list[str]:
    with open(file_path, mode='r') as file:
        read_list: list[str] = file.readlines()
    return [line.strip() for line in read_list if line != '\n']


def test_all(keywords: list[str]):
    fail_output: str = "\n\nthe following tests matched none of the patterns:"

    for keyword in keywords:
        tests: list[str] = text_to_list(f'data/{keyword}/data.txt')
        patterns: list[str] = text_to_list(f'data/{keyword}/patterns.txt')

        for tindex, test in enumerate(tests):
            output: str = f"{keyword}-test{tindex}: \"{test}\""
            for pindex, pattern in enumerate(patterns):
                if re.search(pattern, test, flags=re.I):
                    output = f"{output}, matched with pattern{pindex}"

            if output == f"{keyword}-test{tindex}: \"{test}\"":
                fail_output = f"{fail_output}\n{output}"
                continue
            log.info(output)

    if fail_output == "\n\nthe following tests matched none of the patterns:":
        fail_output = "\n\nall tests matched with a pattern!"
        log.debug(fail_output)
    else:
        log.warning(fail_output)


def test_message(keywords: list[str], message_in: str):
    output: str = f"testing \"{message_in}\" against all keywords:"

    for keyword in keywords:
        patterns: list[str] = text_to_list(f'data/{keyword}/patterns.txt')

        for pindex, pattern in enumerate(patterns):
            if re.search(pattern, message_in, flags=re.I):
                output = f"{output}\n\tmatched with {keyword} pattern{pindex}"

    if output == f"testing \"{message_in}\" against all keywords":
        log.warning("the given message matched with no patterns:")
    else:
        log.debug(output)
