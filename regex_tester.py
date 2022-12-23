import logging
import re


class LocalFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        formats = {
            logging.DEBUG: "\u001b[32m%(message)s\u001b[0m",
            logging.INFO: "\u001b[36m%(message)s\u001b[0m",
            logging.WARNING: "\u001b[31m%(message)s\u001b[0m",
        }
        formatter = logging.Formatter(formats[record.levelno], style="%")
        return formatter.format(record)


handler = logging.StreamHandler()
handler.setFormatter(LocalFormatter())
logging.basicConfig(level=logging.DEBUG, handlers=[handler])
log = logging.getLogger("name")


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

            if highlight_fails:
                if output == f"{keyword}-test{tindex}: \"{test}\"":
                    fail_output += f"\n{output}"
                    continue
            log.info(output)

    if highlight_fails:
        if fail_output == "\n\nthe following tests matched none of the patterns:":
            fail_output = "\n\nall tests matched with a pattern!"
            log.debug(fail_output)
        else:
            log.warning(fail_output)


def test_message(keywords: list[str], message_in: str):
    output: str = f"testing \"{message_in}\" against all keywords"

    for keyword in keywords:
        patterns: list[str] = text_to_list(f'data/{keyword}/patterns.txt')

        for pindex, pattern in enumerate(patterns):
            if re.search(pattern, message_in, flags=re.I):
                output = f"{output}\n\tmatched with {keyword} pattern-{pindex}"

    if output == f"testing \"{message_in}\" against all keywords":
        log.warning("the given message matched with no patterns")
    else:
        log.debug(output)


if __name__ == '__main__':
    keywords_list: list[str] = [
        'ads',
        'aa-overlay',
        'category',
        'hdm',
        'pace',
        'pb',
        'runs',
        'song',
        'view-count',
        'wr',
    ]

    test_keywords(keywords_list, highlight_fails=True)
