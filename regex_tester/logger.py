import logging


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
