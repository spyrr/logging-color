import logging
from colored import fg, bg, attr


cs = lambda f, b: fg(f) + bg(b)


class CustomFormatter(logging.Formatter):
    pre = f'[%(asctime)s][%(name)s][%(levelname)s]{attr(0)}'
    suf = f'{cs(3,0)}(%(filename)s:%(lineno)d){attr(0)}'

    FORMATS = {
        logging.DEBUG: f'📝 {cs(3,0)}{pre} %(message)s {suf}',
        logging.INFO: f'✅ {cs(7,0)}{pre} %(message)s {suf}',
        logging.WARNING: f'🔧 {cs(6,0)}{pre} %(message)s {suf}',
        logging.ERROR: f'⚡ {cs(5,0)}{pre} %(message)s {suf}',
        logging.CRITICAL: f'💀 {cs(15,1)}{pre} %(message)s {suf}',
    }

    def format(self, record):
        fmt = self.FORMATS[record.levelno]
        formatter = logging.Formatter(fmt)
        return formatter.format(record)


#create logger with 'spam_application'
logger = logging.getLogger("My_app")
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")