import argparse

from regex_tester.__init__ import keywords_list
from regex_tester.regex import test_keywords, test_message


def main():
    parser = argparse.ArgumentParser(
        description="interact with the regex repository",
    )
    parser.add_argument('-f', '--full',
                        action='store_true',
                        help="check all saved messages against regex repository"
                        )
    parser.add_argument('-s', '--single',
                        metavar='message',
                        dest='message',
                        type=str,
                        nargs='+',
                        help="check one message against regex repository ")
    parsed_args = parser.parse_args()

    if parsed_args.full:
        test_keywords(keywords_list)
    elif parsed_args.message:
        message = ' '.join(parsed_args.message)
        test_message(keywords_list, message)
