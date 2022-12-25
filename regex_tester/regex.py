import re

from regex_tester.logger import log


def text_to_list(file_path: str) -> list[str]:
    with open(file_path, mode='r') as file:
        read_list: list[str] = file.readlines()
    return [line.strip() for line in read_list if line != '\n']


def test_all(keywords: list[str]):
    passed_tests: int = 0
    failed_tests: int = 0
    fail_output: str = "\n\nthe following tests matched none of the patterns:"

    for keyword in keywords:
        tests: list[str] = text_to_list(f'data/{keyword}/data.txt')
        patterns: list[str] = text_to_list(f'data/{keyword}/patterns.txt')

        for tindex, test in enumerate(tests):
            output: str = f"{keyword}-test{tindex}: \"{test}\""

            for pindex, pattern in enumerate(patterns):
                if re.search(pattern, test, flags=re.I):
                    passed_tests += 1
                    output = f"{output}, matched with pattern{pindex}"

            if output == f"{keyword}-test{tindex}: \"{test}\"":
                failed_tests += 1
                fail_output = f"{fail_output}\n{output}"
                continue

            log.info(output)

    if failed_tests == 0:
        log.debug(f"\n\nall {passed_tests} tests matched with a pattern!")
    else:
        log.warning(f"only {passed_tests} tests passed, there were {failed_tests} that did not")
        log.warning(fail_output)


def test_message(keywords: list[str], message_in: str):
    output: str = f"testing \"{message_in}\" against all keywords:"

    for keyword in keywords:
        patterns: list[str] = text_to_list(f'data/{keyword}/patterns.txt')

        for pindex, pattern in enumerate(patterns):
            if re.search(pattern, message_in, flags=re.I):
                output = f"{output}\n\tmatched with {keyword} pattern{pindex}"

    if output == f"testing \"{message_in}\" against all keywords:":
        log.warning("the given message matched with no patterns")
    else:
        log.debug(output)
